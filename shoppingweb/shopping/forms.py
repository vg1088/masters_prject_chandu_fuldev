# myapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'password1', 'password2')

class SignInForm(forms.Form):
    username = forms.CharField(max_length=254, required=True)
    password = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput)
