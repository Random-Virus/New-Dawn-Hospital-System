from django import forms
from .models import Profile  # Import the Profile model
from django.utils.translation import gettext as _
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'surname', 'email', 'phone', 'id_number', 'date_of_birth', 'medical_aid', 'address', 'city', 'state', 'zip', 'country']

    name = forms.CharField(label=_('Name'), required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    surname = forms.CharField(label=_('Surname'), required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label=_('Email'), required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label=_('Phone'), required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    id_number = forms.CharField(label=_('ID Number'), required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(label=_('Date of Birth'), required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    medical_aid = forms.CharField(label=_('Medical Aid'), required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label=_('Address'), required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label=_('City'), required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(label=_('State'), required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    zip = forms.CharField(label=_('Zip'), required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(label=_('Country'), required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    # You can add custom validation or widgets here if needed


class LanguageSelectorForm(forms.Form):
    language = forms.ChoiceField(
        choices=settings.LANGUAGES,
        label=_("Preferred Language"),
        widget=forms.Select(attrs={'onchange': 'this.form.submit();'})
    )