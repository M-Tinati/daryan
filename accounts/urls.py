# accounts/urls.py
from django.urls import path
from .views import RegisterView, CustomLoginView, CustomLogoutView, ProfileUpdateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def dashboard(request):
    return render(request, "accounts/dashboard.html")

app_name = 'accounts'

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("dashboard/", login_required(dashboard), name="dashboard"),
    path("edit-profile/", ProfileUpdateView.as_view(), name="edit_profile"),
]
