from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
           
            return redirect('index.html')  # Create a profile view to handle user profiles
    else:
        form = UserCreationForm()
    return render(request, 'Auth/register.html', {'form': form})

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

# ... other views ...

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Use the renamed login function
                return redirect('index')  # Redirect to the index page after successful login
            else:
                messages.error(request, "Invalid username or password. Please try again.")
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm()
    return render(request, 'Auth/login.html', {'form': form})

