from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve

# view imports
from login.views import log_in, log_out, signup
from sellyoshit.views import home


class TestUrls(SimpleTestCase):
    """
    Test for urls in users.urls.py
    """

    def test_login_url_resolves(self):
        url = reverse('login')

        self.assertEquals(resolve(url).func, log_in)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, log_out)

    def test_signup_url_resolves(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup)

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)