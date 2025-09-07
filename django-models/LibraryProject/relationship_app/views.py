from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import permission_required, user_passes_test
from .models import Library, Book

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()

class register(CreateView):
    UserCreationForm()
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required("relationship_app.can_add_book")
def add_book(request):
    return render(request, "relationship_app/add_book.html")

@permission_required("relationship_app.can_change_book")
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "relationship_app/edit_book.html", {"book": book})

@permission_required("relationship_app.can_delete_book")
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "relationship_app/delete_book.html", {"book": book})