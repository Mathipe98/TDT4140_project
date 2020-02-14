from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import Users


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=45,help_text="Required")
    email = forms.EmailField(max_length=45,help_text="Required")

    class Meta:
        model = Users
        fields = ("username","email","password1","password2","firstname","lastname")

class LoginForm:
     class Meta: