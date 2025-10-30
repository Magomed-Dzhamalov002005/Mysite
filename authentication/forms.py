from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, label="password")
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2'] # Aaand any other fields