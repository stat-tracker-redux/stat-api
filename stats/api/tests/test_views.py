from django.http import HttpRequest
from django.test import TestCase
from api.views import user_create
from django.contrib.auth.models import User


class UserViewsTest(TestCase):
    def test_register_url_returns_empty_string(self):
        """
        Tests that a request to the register url returns nothing
        """
        request = HttpRequest()
        response = user_create(request)
        self.assertEqual(response.content, b'')

    def test_register_url_requires_post(self):
        """
        Tests that POST requests get through, but others do not
        """
        post_request = HttpRequest()
        post_request.method = 'POST'
        get_request = HttpRequest()
        post_response = user_create(post_request)
        get_response = user_create(get_request)
        self.assertEqual(post_response.status_code, 200)
        self.assertNotEqual(get_response.status_code, 200)

    def test_register_url_creates_user(self):
        """
        Tests that the view creates a user in the database
        """
        post_request = HttpRequest()
        post_request.method = 'POST'
        post_request.POST['username'] = 'brother.bear'
        post_request.POST['password'] = 'password'
        post_request.POST['email'] = 'brother@berenstain.com'
        response = user_create(post_request)
        self.assertEqual(User.objects.get(username='brother.bear').email,
                         'brother@berenstain.com')
        self.assertEqual(User.objects.get(email='brother@berenstain.com').username,
                         'brother.bear')
