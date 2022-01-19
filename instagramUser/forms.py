from dataclasses import fields
from statistics import mode
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile

class SignUpForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username','email','first_name','password1','password2')

class LoginForm(AuthenticationForm):
    class Meta:
        model = Profile
        fields = ('username','password1')