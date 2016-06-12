from django.http import HttpRequest
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from api.views import user_create, logout


class UserViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.username = 'test'
        self.email = 'test@email.com'
        self.password = 'password'
        user = User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password
        )
        user.save()
        token = Token.objects.create(user=user)
        token.save()
        self.token = token.key

    def test_register_url_returns_empty_string(self):
        """
        Tests that a request to the register url returns nothing
        """
        request = self.factory.get('/register/')
        response = user_create(request)
        self.assertEqual(response.content, b'')

    def test_register_url_post_with_good_json_returns_200(self):
        """
        Tests that POST requests get through to register endpoint
        and that the POST has the correct format
        """
        json_string = '{"username": "user", "email": "user@email.com", "password": "supersecret"}'
        post_request = self.factory.post('/register/', content_type='application/json', data=json_string)
        post_response = user_create(post_request)
        self.assertEqual(post_response.status_code, 200)

    def test_register_url_good_post_creates_user(self):
        """
        Tests that a POST request with the correct JSON format
        creates a new user
        """
        json_string = '{"username": "user", "email": "user@email.com", "password": "supersecret"}'
        post_request = self.factory.post('/register/',
                                         content_type='application/json',
                                         data=json_string)
        post_response = user_create(post_request)
        self.assertEqual(User.objects.get(username='user').email,
                         "user@email.com")

    def test_register_url_get_returns_error(self):
        """
        Tests that GET requests to register endpoint return errors
        """
        get_request = self.factory.get('/register/')
        get_response = user_create(get_request)
        self.assertNotEqual(get_response.status_code, 200)

    def test_register_url_bad_json_returns_400_error(self):
        """
        Tests that a POST request with an improperly formatted
        JSON returns a 400 error
        """
        json_string = '{"nothing": "my bad JSON"}'
        post_request = self.factory.post('/register/',
                                         content_type='application/json',
                                         data=json_string)
        post_response = user_create(post_request)
        self.assertEqual(post_response.status_code, 400)

    def test_register_url_bad_json_returns_custom_message(self):
        """
        Tests that a POST request with an improperly formatted
        JSON returns a custom error message
        """
        json_string = '{"nothing": "my bad JSON"}'
        post_request = self.factory.post('/register/',
                                         content_type='application/json',
                                         data=json_string)
        post_response = user_create(post_request)
        self.assertEqual(post_response.content,
                         b'Please use the correct JSON format')

    def test_logout_url_get_requests_return_405_error(self):
        """
        Tests that get requests to logout view return error
        """
        request = self.factory.get('/api/logout/')
        response = logout(request)
        self.assertEqual(response.status_code, 405)
        #TODO: refactor to test for failing of authenticated GET request

    def test_logout_url_non_authenticated_post_requests_return_403(self):
        """
        Tests that non-authenticated post requests to logout view fail
        """
        request = self.factory.post('/api/logout/')
        response = logout(request)
        self.assertEqual(response.status_code, 403)

    def test_logout_url_authenticated_post_requests_return_200(self):
        """
        Tests that authenticated post requests to logout view
        return 200 OK Code
        """
        request = self.factory.post('/api/logout/',
                                    content_type='application/json',
                                    headers={'Authorization':
                                             'Token ' + self.token},
                                    data={'username': self.username,
                                          'password': self.password})
        response = logout(request)
        self.assertEqual(response.status_code, 200)
