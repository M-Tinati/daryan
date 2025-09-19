from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("phone", "username", "first_name", "last_name", "city",)
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500'}),
            'username': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500'}),
            'first_name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500'}),
            'city': forms.Select(attrs={'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500'}),
        }

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="شماره تلفن",
        widget=forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500'})
    )

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'city']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500'}),
            'city': forms.Select(attrs={'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address']
        widgets = {
            'address': forms.Textarea(attrs={
                'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500',
                'rows': 3
            }),
        }
