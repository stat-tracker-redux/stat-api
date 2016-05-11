from django.http import HttpRequest
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from api.views import user_create


class UserViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='test', email='test@email.com', password='password'
        )

    def test_register_url_returns_empty_string(self):
        """
        Tests that a request to the register url returns nothing
        """
        request = self.factory.get('/register/')
        response = user_create(request)
        self.assertEqual(response.content, b'')

    def test_register_url_post_returns_200(self):
        """
        Tests that POST requests get through to register endpoint
        """
        # json_string = '{"username": "user", "email": "user@email.com", "password": "supersecret"}'
        json_string = '{"things": "stuff"}'
        post_request = self.factory.post('/register/', content_type='application/json', data=json_string)
        post_response = user_create(post_request)
        self.assertEqual(post_response.status_code, 200)

    def test_register_url_get_returns_error(self):
        """
        Tests that GET requests to register endpoint return errors
        """
        get_request = self.factory.get('/register/')
        get_response = user_create(get_request)
        self.assertNotEqual(get_response.status_code, 200)
