from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length =200)
    author = models.CharField(max_length= 100)
    publication_year = models.IntegerField()

class CustomUser(AbstractUser):
    date_of_birth= models.DateField()
    profile_photo= models.ImageField(upload_to= 'profile_pics/', null=True, blank= True)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be filled')
        # normalize email (makes it lowercase)
        email= self.normalize_email(email)

        # create user object
        user = self.model(email=email, **extra_fields)
        user.set_password(password)   # hash the password
        user.save(using=self._db)     # save to database
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email, password, **extra_fields)


