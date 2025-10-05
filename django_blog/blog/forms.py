from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment

class RegisterForm(UserCreationForm):
    email=forms.CharField(max_length=200, required=True)

    class Meta:
        model= User
        fields=['username', 'email','first_name','last_name', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    bio=forms.CharField(widget=forms.Textarea, required=False)
    profile_picture= forms.ImageField(required=False)
    model= User
    fields=['first_name', 'last_name', 'email','bio','profile_picture']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']