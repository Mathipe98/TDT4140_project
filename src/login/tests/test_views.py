from django.test import TestCase, Client
from django.urls import reverse, resolve
from users.models import *
import json


class TestViews(TestCase):
    """
    Test for views in login.views.py, tests the following:
        - client receives the url for each view
        - response code for HTTP GET is 200 OK when doing HTTP-requests
        - response code is 302 when doing HTTP-redirect
        - the template is correct, e.g. sellyoshit/.../<file>.html
    """

    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.log_in_url = reverse('login')
        self.log_out_url = reverse('logout')

    def test_signup_GET(self):
        response = self.client.get(self.signup_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sellyoshit/log_inEXT.html')

    def test_log_in_GET(self):
        response = self.client.get(self.log_in_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sellyoshit/log_inEXT.html')

    def test_log_out_GET(self):
        response = self.client.get(self.log_out_url)

        # Logout is redirected to home, thus the HTTP status code should be 302
        self.assertEquals(response.status_code, 302)