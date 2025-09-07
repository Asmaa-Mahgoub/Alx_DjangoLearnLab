from django.db import models


from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.
class Author(models.Model):
    name= models.CharField(max_length =100)

    def __str__(self):
        return self.name 

class Book(models.Model):
    title= models.CharField(max_length = 100)
    author= models.ForeignKey(Author, on_delete= models.CASCADE, related_name="books")

    def __str__(self):
        return self.name 

class Library(models.Model):
    name= models.CharField(max_length= 100)
    books= models.ManyToManyField(Book, related_name="library")

    def __str__(self):
        return self.name 

class Librarian(models.Model):
    name= models.CharField(max_length= 100)
    library= models.OneToOneField(Library,on_delete=models.CASCADE, related_name= "librarian")

    def __str__(self):
        return self.name 

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Admin'),
        ('library_member', 'Library Member'),
        ('librarian', 'Librarian'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

class UserProfile(models.Model):
    role = models.CharField(max_length=100 , choices=[('Admin')])
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)