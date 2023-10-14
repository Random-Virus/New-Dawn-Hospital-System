from django.shortcuts import render
from .forms import ProfileForm, LanguageSelectorForm
from .models import profile
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserChangeForm 
from django.contrib.auth import update_session_auth_hash
# Create your views here.


def index(request):
    return render(request, 'home/index.html')
@login_required
def profile_view(request):
    user = request.user
    try:
        user_profile = profile.objects.get(user=user)
    except profile.DoesNotExist:
        user_profile = None
    
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'home/profile.html', context)
    
@login_required
def profile_edit(request):
    user = request.user
    try:
        user_profile = profile.objects.get(user=user)
    except profile.DoesNotExist:
        user_profile = None
    if request.method =='POST':
        profile_form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=user_profile)

    context = {
        'profile_form': profile_form,
        'user_profile': user_profile,
        'LanguageSelectorForm': LanguageSelectorForm,
    }
    return render(request, 'home/profile_edit.html', context)

def login(request):
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