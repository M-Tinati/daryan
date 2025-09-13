from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("phone", "username", "first_name", "last_name", "city",)

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="شماره تلفن")
    password = forms.CharField(widget=forms.PasswordInput)
