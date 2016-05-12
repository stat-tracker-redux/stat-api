from django.http import HttpRequest
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from api.views import user_create


class UserViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        # self.user = User.objects.create_user(
        #     username='test', email='test@email.com', password='password'
        # )

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
