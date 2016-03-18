from django.test import TestCase, LiveServerTestCase

from requests import get, post


class UserExperienceTestCase(LiveServerTestCase):
    def test_can_create_a_new_user(self):
        """
        Test that the /register/ endpoint can succesfully create a new user
        """
        # Todd registers with his email and password
        register_resp = get(self.live_server_url + '/register/',
                            data={"username": "superlunk360",
                                  "email": "todd.mcbuffy@gmail.com",
                                  "password": "supersecret"})
        self.assertEquals(register_resp.status_code, 200)
        self.assertEquals(register_resp.text, '')
