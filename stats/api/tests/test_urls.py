from django.test import TestCase

from django.core.urlresolvers import resolve

from api.views import user_create

# Create your tests here.


class UserURLsTest(TestCase):
    def test_register_url_resolves_to_user_create_view(self):
        """
        Tests that /register/ endpoint resolves to a view titled user_create
        """
        found_user_create = resolve('/register/')
        self.assertEqual(found_user_create.func, user_create)
