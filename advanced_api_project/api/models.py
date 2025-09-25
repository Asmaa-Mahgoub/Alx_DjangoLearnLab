from django.db import models

# Create your models here.

class Author(models.Model):
    name= models.CharField(max_length= 100)

class Book(models.Model):
    title= models.CharField(max_length= 100)
    publication_year= models.IntegerField()
    author= models.ForeignKey(Author, related_name= 'books' ,on_delete= models.CASCADE)

def __str__():
    return f"self.title by self.name"

# ForeignKey creates a relationship to Author.
# # Each book belongs to ONE author, but one author can have MANY books.