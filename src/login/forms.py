"""
    Form for registrations and logging in to website using the User model

    classes:
        SignupForm : UserCreationForm
            Form which allows you to register a new user on the website through the User model
         LoginForm : forms.ModelForm
            Form which allows you to log in to an existing user on thw website
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from users.models import Users


class SignupForm(UserCreationForm):
    """
        Form for creating a new user
    """
    username = forms.CharField(max_length=45, help_text="Required")
    email = forms.EmailField(max_length=45, help_text="Required")

    class Meta:
        """
            Meta class for the registration form

            Attributes
                model : Model
                    User model
                fields : Tuple
                    The fields to register with in the User model
        """
        model = Users
        fields = ("username", "email", "password1", "password2", "firstname", "lastname")


class LoginForm(forms.ModelForm):
    """
        Form for logging in with an existing user

        Functions
            clean : None
                Cleans the inputted username and password, and checks if the user exist.
    """
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        """
            Meta class for the registration form

            Attributes
                model : Model
                    User model
                fields : Tuple
                    The fields to log in with in the User model
        """
        model = Users
        fields = ['username', 'password']

    def clean(self):
        """
        Cleans the inputted username and password, and checks if the user exist.

        :param self: The form itself
        :return: None
        """
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid login")
