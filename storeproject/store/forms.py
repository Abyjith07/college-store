from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'cpassword']
