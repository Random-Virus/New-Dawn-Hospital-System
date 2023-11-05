from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.utils import translation
from allauth.socialaccount.models import SocialAccount
from .forms import UpdateProfileForm, LanguageSelectorForm, SignUpForm
from .models import Profile
from appointment.models import Appointment
from datetime import date

def index(request):
    return render(request, 'home/index.html')

@login_required
def profile_view(request):
    user = request.user
    user_profile, created = Profile.objects.get_or_create(user=user)

    google_account = None

    if not created:
    # Check if the user has a linked Google account
     google_account = SocialAccount.objects.filter(provider='google', user=user).first()

    if google_account:
        # If the user has a linked Google account, fetch Google account data
        google_data = google_account.extra_data

        # Update the user's profile with Google data
        user_profile = user.profile  # Ensure user_profile is correctly associated with the user

        user_profile.name = google_data.get('given_name', user_profile.name)
        user_profile.surname = google_data.get('family_name', user_profile.surname)
        user_profile.email = google_data.get('email', user_profile.email)
        user_profile.phone = google_data.get('phone_number', user_profile.phone)
        user_profile.id_number = google_data.get('id_number', user_profile.id_number)
        user_profile.date_of_birth = google_data.get('date_of_birth', date(1999, 1, 1))
        user_profile.medical_aid = google_data.get('medical_aid', user_profile.medical_aid)
        user_profile.address = google_data.get('address', user_profile.address)
        user_profile.city = google_data.get('city', user_profile.city)
        user_profile.state = google_data.get('state', user_profile.state)
        user_profile.zip = google_data.get('zip', user_profile.zip)
        user_profile.country = google_data.get('country', user_profile.country)
        user_profile.save()


    context = {
        'user_profile': user_profile,
    }
    return render(request, 'home/profile.html', context)

@login_required
def viewAppointment(request):
    # Filter appointments for the currently logged-in user
    appointments = Appointment.objects.filter(email=request.user.email)

    context = {
        'appointments': appointments,
    }

    return render(request, 'home/view_appointments.html', context)


@login_required
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)  # Get the user's profile
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=profile)  # Use the user's profile as the instance

        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = UpdateProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'home/profile_edit.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Create a new user
            auth_login(request, user)  # Log in the user
            return redirect('profile_view')
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
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'home/signin.html')

def logout(request):
    auth_logout(request)
    return redirect('/')

def set_language(request):
    if request.method == 'POST':
        form = LanguageSelectorForm(request.POST)
        if form.is_valid():
            language = form.cleaned_data['language']
            request.session[translation.LANGUAGE_SESSION_KEY] = language
    return redirect(request.META.get('HTTP_REFERER'))

def blog(request):
    return render(request, 'blog/index.html')
