from django.shortcuts import render
from .forms import UpdateProfileForm, LanguageSelectorForm, SignUpForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserChangeForm 
from django.contrib.auth import update_session_auth_hash
# Create your views here.


def index(request):
    return render(request, 'home/index.html')
    
@login_required
def profile_view(request):
    user = request.user
    try:
        user_profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        user_profile = None
    
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'home/profile.html', context)
    
@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user.profile)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = UpdateProfileForm(instance=request.user.profile)

    context = {
        'form': form,
        
    }
    return render(request, 'home/profile_edit.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Create a new user
            login(request, user)  # Log in the user
            return redirect('profile_view')  # Replace 'profile' with your desired URL name
    else:
        form = SignUpForm()
    return render(request, 'home/signup.html', {'form': form})
    
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            user = form.get_user()
            auth_login(request, user)  # Log in the user
            print('if')
            # Redirect to a success page
            return redirect('index')  # Replace 'profile' with your desired URL name
    else:
        print('else')
        form = AuthenticationForm()
    return render(request, 'home/signin.html')

def logout(request):
    logout(request)
    return redirect('/')


def set_language(request):
    if request.method == 'POST':
        form = LanguageSelectorForm(request.POST)
        if form.is_valid():
            language = form.cleaned_data['language']
            request.session[translation.LANGUAGE_SESSION_KEY] = language
    return redirect(request.META.get('HTTP_REFERER'))
    return render(request, 'appointment/appointment.html')

def blog(request):

    return render(request, 'blog/index.html')
