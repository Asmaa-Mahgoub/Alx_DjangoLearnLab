from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import has_permission
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Book
from .forms import ExampleForm

["book-list", "raise_exception", "books"]
["from .forms import ExamplesForm"]
@permission_required('app_name.can_edit', raise_exception=True)
def edit_view(request, pk):
    return render(request, 'edit_template.html')

def edit_view(request, pk):
    if not has_permission(request.user, 'app_name.can_edit'):
        return redirect('permission_denied')
    return render(request, 'edit_template.html')

def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/book_list.html', context)

