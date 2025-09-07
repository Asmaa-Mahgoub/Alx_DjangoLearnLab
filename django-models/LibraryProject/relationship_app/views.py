from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
# Create your views here.

#Create a function that lists all books stored in the database.
#This view should render a simple text list of book titles and their authors.
def list_books(request):
   books= Book.objects.all()
   context = {'books': books}
   return render(request, 'relationship_app/list_books.html', context) 


class LibraryDetailView(DetailView):
    """Displays details for a specific library including all its books."""
    model = Library
    template_name = 'relationship_app/library_detail.html'  
    

    def get_context_data(self, **kwargs):
        """Add all books in this library to context."""
        context = super().get_context_data(**kwargs)
        library = self.get_object()  # the current Library instance
        context['books'] = library.books.all()  # all books in this library
        return context
    
    def get_queryset(self):
        return super().get_queryset().prefetch_related('books_author')