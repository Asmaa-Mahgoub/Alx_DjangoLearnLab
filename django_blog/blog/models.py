from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=200)
    content= models.TextField()
    published_date= models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(User, on_delete=models.CASCADE) 

""" from django.contrib.auth.models import User
This imports Django’s built-in User model, which is provided automatically when you create a Django project.

That default model already includes:
username, password, email, first_name, last_name, is_staff, is_superuser, date_joined, last_login, and more…

So basically, it’s a ready-to-use model for handling authentication, login, and user management.
We can use Django’s built-in User model if we don’t need custom fields or roles & only need basic 
login/registration, e.g.:

username + password authentication

admin site management

simple permissions """






 