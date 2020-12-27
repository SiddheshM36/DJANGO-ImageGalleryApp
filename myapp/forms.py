from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Image
from django.contrib.auth.models import User

class UserRegistration(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']