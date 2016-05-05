from django.http import HttpRequest
from django.test import TestCase
from api.views import user_create


class UserViewsTest(TestCase):
    def test_register_url_returns_empty_string(self):
        """
        Tests that a request to the register url returns nothing
        """
        request = HttpRequest()
        response = user_create(request)
        self.assertEqual(response.content, b'')

    def test_register_url_post_returns_200(self):
        """
        Tests that POST requests get through to register endpoint
        """
        post_request = HttpRequest()
        post_request.method = 'POST'
        post_response = user_create(post_request)
        self.assertEqual(post_response.status_code, 200)

    def test_register_url_get_returns_error(self):
        """
        Tests that GET requests to register endpoint return errors
        """
        get_request = HttpRequest()
        get_response = user_create(get_request)
        self.assertNotEqual(get_response.status_code, 200)
