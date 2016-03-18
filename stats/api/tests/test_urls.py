from django.test import TestCase

from django.core.urlresolvers import resolve

from api.views import create_user

# Create your tests here.


class UserURLsTest(TestCase):
    def test_register_url_resolves_to_create_user_view(self):
        """
        Tests that /register/ endpoint resolves to a view titled create_user
        """
        found_create_user = resolve('register')
        self.assertEqual(found_create_user.func, create_user)
