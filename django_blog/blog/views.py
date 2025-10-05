from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from .forms import PostForm, RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import *
from django.db.models import Q

from django.views.generic import  ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class RegisterView(CreateView):
    def signup(request):
        if request.method == "Post":
            form=RegisterForm(request.POST) #This line takes the form data that came from the browser and creates a form object filled with user’s info.
            if form.is_valid:
                form.save()
            login(request.user)  # auto login after registration
            return redirect('home/')
        else:
            form=RegisterForm()
            return render(request, 'blog/register.html', {'form': form})

class LoginView(LoginView):
    def login_view(request):
        if request.method == "POST":
            form = ProfileForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()       # Get the logged-in user
                login(request, user)         # Create session for user
                messages.success(request, "Logged in successfully!")
                return redirect('home')      # Redirect after login
        else:
            form = ProfileForm()      # Empty login form
            return render(request, 'blog/login.html', {'form': form})
        
@login_required
def profile_view(request):
    user = request.user  # Get the currently logged-in user
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user)  # Fill form with submitted data
        if form.is_valid():
            form.save()  # Save the updated user info
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')  # Refresh the page after saving
    else:
        form = ProfileForm(instance=user)  # Pre-fill the form with existing user info
    return render(request, 'blog/profile.html', {'form': form})


class LogoutView(LogoutView):
    def logout_view(request):
        logout(request)                  # Destroys the session
        messages.info(request, "You have been logged out.")
        return redirect('login')         # Back to login page
     

       
class PostListView(ListView):
    """Displays a list of all blog posts."""
    model = Post
    template_name = 'blog/post_list.html'   # Template to render
    context_object_name = 'posts'           # Variable name used in template
    ordering = ['-published_date']          # Show newest first        
#When a user opens /posts/, Django fetches all posts from the database and passes them to post_list.html as a list named posts       

class PostDetailView(DetailView):
    """Displays details for a single post."""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
#When a user clicks on a post title → /posts/5/, Django fetches the post with id=5 and shows it in post_detail.html
    def get_context_data(self, **kwargs):
        """Inject post comments and form into context."""
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = Comment.objects.filter(post=post).order_by('-created_at')
        context['form'] = CommentForm()
        return context

# Add a Comment
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, id=post_id)
        form.instance.post = post
        form.instance.author = self.request.user
        messages.success(self.request, 'Comment added successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})
# Edit Comment
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Allows the author to edit their comment."""
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        messages.success(self.request, 'Comment updated successfully!')
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})

# Delete Comment
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Allows the author to delete their comment."""
    model = Comment
    template_name = 'blog/delete_comment.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        messages.success(self.request, 'Comment deleted successfully!')
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})
class PostCreateView(LoginRequiredMixin, CreateView):
    """Allows authenticated users to create new posts."""
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')  # Redirect after saving

    def form_valid(self, form):
        form.instance.author = self.request.user  # Assign logged-in user as author
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Allows post authors to edit their posts."""
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only author can edit
#The author clicks “Edit” → form appears with old data → they update content → click “Save” → Django updates the database record.

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Allows authors to delete their posts."""
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only author can delete
#User clicks “Delete” → confirmation page appears → confirms → post removed → redirected to post list.

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag = self.kwargs.get('tag')
        #return Post.objects.filter(tag__name__in=[tag])
        return Post.objects.filter(tags__name__icontains=[tag])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs.get('tag')
        return context
    
    def search_posts(request):
        query = request.GET.get('q')
        results = Post.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)
        ).distinct()
        return render(request, 'blog/search_results.html', {'results': results})