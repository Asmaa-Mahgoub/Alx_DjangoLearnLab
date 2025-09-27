from django.urls import path
from .views import ListView,CreateView,DetailView,DeleteView,UpdateView
urlpatterns=[
    path('/books/',ListView.as_view, name='list_books'),
    path('/books/create/',CreateView.as_view, name='create_books'),
    path('/books/<int:pk>/',DetailView.as_view, name='book_details'),
    path('/books/delete/<int:pk>/',DeleteView.as_view, name='book_delete'),
    path('/books/update/<int:pk>/',UpdateView.as_view, name='book_update'),
]