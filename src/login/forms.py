from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from users.models import Users


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=45, help_text="Required")
    email = forms.EmailField(max_length=45, help_text="Required")

    class Meta:
        model = Users
        fields = ("username", "email", "password1", "password2", "firstname", "lastname")


class LoginForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['username', 'password']

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid login")
