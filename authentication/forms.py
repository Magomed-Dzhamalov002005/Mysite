from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, label="password")
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2'] # Aaand any other fields


class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password', 'email']