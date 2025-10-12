from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    bio=models.TextField(blank=True)
    profile_picture=models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    followers=models.ManyToManyField('self', related_name='following',symmetrical=False )

def __str__(self):
        return self.username


#symmetrical=False means if A follows B, B doesn’t automatically follow A.

""" The related_name defines how the opposite side of the relationship can access this connection.
Without related_nameIf you didn’t specify it, Django would try to name it automatically (and sometimes that name conflicts).

With related_name='following'

It means:

From a user object,
user.followers.all() → shows all users who follow this user.
user.following.all() → shows all users that this user follows.
So, the related_name gives a reverse access name for the same relationship. """


""" from accounts.models import CustomUser

a = CustomUser.objects.create(username="A")
b = CustomUser.objects.create(username="B")
c = CustomUser.objects.create(username="C")

a.following.add(b)  # A follows B
a.following.add(c)  # A follows C """
