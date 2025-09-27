from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from .models import Book
from .serializers import BookSerializer
# Create your views here.

#Listing books
class BookListView(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    filter_backends=[
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_fields=['title', 'publication_year', 'author']
    search_fields=['title', 'author']
    ordering_fields=['title', 'publication_year']
    ordering=['title']

#Creating new books
class CreateView(generics.CreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[permissions.IsAuthenticated]

# Retrieve by ID
class DetailView(generics.RetrieveAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

#Deleting existing books
class DeleteView(generics.DestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[permissions.IsAuthenticated]

#Updating existing books
class UpdateView(generics.UpdateAPIViewAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[permissions.IsAuthenticated]