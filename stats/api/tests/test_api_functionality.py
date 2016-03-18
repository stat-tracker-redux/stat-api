from django.test import TestCase, LiveServerTestCase

from requests import get, post


class UserExperienceTestCase(LiveServerTestCase):
    def test_can_create_a_new_user(self):
        register_resp = get(self.live_server_url + '/register/')
        self.assertEquals(register_resp.status_code, 200)
        self.assertEquals(register_resp.text, '')
