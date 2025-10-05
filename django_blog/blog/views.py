from django.shortcuts import redirect, render
from .models import Post
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from .forms import PostForm, RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required

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
     

       
        
            
  
    


