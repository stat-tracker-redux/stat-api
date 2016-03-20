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
