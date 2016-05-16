from requests import get, post
import json

from django.test import TestCase, LiveServerTestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserExperienceTestCase(LiveServerTestCase):
    def setUp(self):
        """
        Create a user for login/logout tests
        """
        self.username = 'exists'
        self.email = 'exists@email.com'
        self.password = 'thispassword'
        user = User.objects.create_user(username=self.username,
                                        email=self.email,
                                        password=self.password
                                        )
        user.save()
        token = Token.objects.create(user=user)
        token.save()
        self.token = token.key

    def test_can_create_a_new_user(self):
        """
        Test that the /register/ endpoint can succesfully create a new user
        """
        # Todd registers with his email and password
        register_resp = post(self.live_server_url + '/register/',
                             data=json.dumps({"username": "superlunk360",
                                              "email": "todd.mcbuffy@gmail.com",
                                              "password": "supersecret"}))
        self.assertEquals(register_resp.status_code, 200)
        self.assertEquals(register_resp.text, '')

        self.assertEqual(User.objects.get(username='superlunk360').email,
                         'todd.mcbuffy@gmail.com')
        self.assertEqual(User.objects.get(
                         email='todd.mcbuffy@gmail.com').username,
                         'superlunk360')

    def test_user_can_login(self):
        """
        Test that an existing user can login at /api/login/ endpoint
        """
        login_resp = post(self.live_server_url + '/api/login/',
                          data={"username": self.username,
                                "password": self.password})
                                # TODO: figure out why json doesn't work here
        self.assertEqual(login_resp.status_code, 200)
        self.assertEqual(login_resp.json()['token'], self.token)


    def test_user_can_logout(self):
        """
        Test that a logged-in user can logout at /api/logout/
        """
        logout_resp = post(self.live_server_url + '/api/logout/',
                           data=json.dumps({"username": self.username,
                                            "password": self.password}),
                           headers={'Authorization':
                                    'access_token ' + self.token})
        self.assertEqual(logout_resp.status_code, 200)
