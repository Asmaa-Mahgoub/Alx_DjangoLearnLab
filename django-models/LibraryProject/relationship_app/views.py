from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library
# Create your views here.

#Create a function that lists all books stored in the database.
#This view should render a simple text list of book titles and their authors.
def list_books(request):
   books= Book.objects.all()
   context = {'book_list': books}
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