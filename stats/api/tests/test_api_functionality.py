from requests import get, post
import json

from django.test import TestCase, LiveServerTestCase
from django.contrib.auth.models import User


class UserExperienceTestCase(LiveServerTestCase):
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
