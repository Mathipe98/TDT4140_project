from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from django import forms

# views imports
from login.views import log_in, log_out, signup

# forms imports
from .forms import SignupForm

# models import from users directory in order to test register-login
from users.models import Users


class TestRegisterLogin(TestCase):
    """This class is creating a new user and then tests that you are able to login"""
    def setUp(self):
        self.credentials = {
            'username': 'Georgyyy',
            'email': 'georgyboy@gmail.com',
            'password': 'a2bC90PqL345',
            'firstname': 'George',
            'lastname': 'Mc Twist'}
        Users.objects.create_user(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)


class TestForms(TestCase):
    """
    This class tests the input fields in the form that is used when signing up a new user. It also tests that you
    can't register a user with a username that has already been used.
    """

    def test_signup_form_valid_data(self):
        form = SignupForm(data={
            'username': 'Georgyyy',
            'email': 'georgyboy@gmail.com',
            'password1': 'a2bC90PqL345',
            'password2': 'a2bC90PqL345',
            'firstname': 'George',
            'lastname': 'Mc Twist'
        })

        self.assertTrue(form.is_valid())

    def test_signup_form_not_valid_email(self):
        form = SignupForm(data={
            'username': 'Georgyyy',
            'email': 'georgyboy',
            'password1': 'a2bC90PqL345',
            'password2': 'a2bC90PqL345',
            'firstname': 'George',
            'lastname': 'Mc Twist'
        })

        self.assertFalse(form.is_valid())

    def test_signup_form_not_equal_password(self):
        form = SignupForm(data={
            'username': 'Georgyyy',
            'email': 'georgyboy@gmail.com',
            'password1': 'a2bC90PqL345678',
            'password2': 'a2bC90PqL345',
            'firstname': 'George',
            'lastname': 'Mc Twist'
        })

        self.assertFalse(form.is_valid())

    def test_signup_form_blank_username(self):
        form = SignupForm(data={
            'username': '',
            'email': 'georgyboy@gmail.com',
            'password1': 'a2bC90PqL345',
            'password2': 'a2bC90PqL345',
            'firstname': 'George',
            'lastname': 'Mc Twist'
        })

        self.assertFalse(form.is_valid())

    def test_signup_form_to_common_password(self):
        form = SignupForm(data={
            'username': 'Georgyyy',
            'email': 'georgyboy@gmail.com',
            'password1': 'hello123',
            'password2': 'hello123',
            'firstname': 'George',
            'lastname': 'Mc Twist'
        })

        self.assertFalse(form.is_valid())

    def test_signup_form_username_already_used(self):
        self.credentials = {
            'username': 'Georgyyy',
            'email': 'georgyboy@gmail.com',
            'password': 'a2bC90PqL345',
            'firstname': 'George',
            'lastname': 'Mc Twist'}
        Users.objects.create_user(**self.credentials)

        # Trying to make make this form should cause an ValidationError because the username already exists.
        test_form = SignupForm(data={
            'username': 'Georgyyy',
            'email': 'georgyboy@gmail.com',
            'password1': 'a2bC90PqL345',
            'password2': 'a2bC90PqL345',
            'firstname': 'George',
            'lastname': 'Mc Twist'
        })

        self.assertFalse(test_form.is_valid())
        self.assertRaises(forms.ValidationError)


class TestViews(TestCase):
    """
    This class is testing the HTTP-response from the views. 200 OK if new HTML, or 302 if redirect. 400 is no response.
    It also assures that the templates are correct.
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

        self.assertEquals(response.status_code, 302)        # Logout is redirected to home


class TestUrls(SimpleTestCase):
    """
    This class is testing the urls for logging in and out, as well as signup page. These urls and views are contained
    in sellyoshit directory. Reverse returns the url if it exists within the project, and the url should have a func-
    method that corresponds to the correct view.
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
