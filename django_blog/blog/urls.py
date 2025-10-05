from django.urls import path
from .views import *

urlpattern=[
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile_view(), name='profile'),
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='update_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
    path('search/', PostByTagListView.as_view(), name='search-posts'),
]
