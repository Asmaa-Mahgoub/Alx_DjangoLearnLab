from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class CustomUserCreationForm(UserCreationForm):
    email=forms.CharField(required=True)

    class Meta:
        model= User
        fields=['username', 'email','first_name','last_name', 'password1', 'password2']