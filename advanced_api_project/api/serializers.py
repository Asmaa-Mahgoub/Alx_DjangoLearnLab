from rest_framework import serializers
from .models import Author, Book

# Converts Book model instances into JSON and validates input data when creating/updating books.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields= '__all__'  # Serialize all fields: title, publication_year, author
    def validation(self, data):
        if data.publication_year > 2025:
            return serializers.ValidationError("Publication Year can't be in future")
        return data


class AuthorSerializer(serializers.ModelSerializer):
    books=BookSerializer(many=True, read_only= True)
    class Meta:
        model= Author
        fields= ['id','name', 'books']


"""
    - In models.py, Book has a ForeignKey to Author.
    - Django automatically creates a reverse relationship: author.books (because of related_name="books").
    - Here, we use that reverse relationship in the AuthorSerializer.
    - Result: When serializing an Author, we also show all of their books inside "books"."""


