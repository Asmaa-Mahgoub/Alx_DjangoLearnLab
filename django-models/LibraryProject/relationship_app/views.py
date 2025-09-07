from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login

from django.contrib.auth.decorators import user_passes_test

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
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        """Add all books in this library to context."""
        context = super().get_context_data(**kwargs)
        library = self.get_object()  # the current Library instance
        context['books'] = library.books.all()  # all books in this library
        return context
    
    def get_queryset(self):
        return super().get_queryset().prefetch_related('books')
    
class register(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')  
    template_name = 'relationship_app/register.html'

def is_Admin(user):
    return user.is_authenticated and user.role == 'Admin'
    @login_required
    @user_passes_test(is_Admin)
    
    def Admin_only_view(request):
        return render(request, 'admin_view.html')

def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    # This view is only accessible to users with the 'Admin' role
    return render(request, 'relationship_app/admin_view.html')  # You can customize the template as needed

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    # This view is only accessible to users with the 'Librarian' role
    return render(request, 'relationship_app/librarian_view.html') 

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    # This view is only accessible to users with the 'Member' role
    return render(request, 'relationship_app/member_view.html')  