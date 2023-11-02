from django import forms
from .models import profile  # Import the Profile model
from django.utils.translation import gettext as _
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
class ProfileForm(forms.ModelForm):
     
    class Meta:
        model = profile  # Associate the form with the Profile model
        fields = ['name', 'surname', 'email', 'phone','id_number', 'date_of_birth', 'address', 'city', 'state', 'zip', 'country', 'user']

    # You can add custom validation or widgets here if needed


class LanguageSelectorForm(forms.Form):
    language = forms.ChoiceField(
        choices=settings.LANGUAGES,
        label=_("Preferred Language"),
        widget=forms.Select(attrs={'onchange': 'this.form.submit();'})
    )