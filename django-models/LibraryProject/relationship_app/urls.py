from django.urls import path
from .views import list_books, LibraryDetailView

from django.contrib.auth.views import LoginView 
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from .views import register_librarian, get_librarian_for_library
from .views import register
from .import views


urlpatterns = [
    path('books/', list_books, name= 'list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

 # Authentication
    path('login/', LoginView.as_view(template_name='')),
    path('logout/', LogoutView.as_view(template_name='')),
    path('register/', views.register.as_view(), name='register'),
 # Role-based dashboards
    path('Admin-dashboard/', views.Admin_only_view, name='Admin_dashboard'),
    path('librarian/',  views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('Admin-dashboard/', views.admin_view, name='Admin_dashboard'),
]