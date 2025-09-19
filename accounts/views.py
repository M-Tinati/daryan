from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    ProfileForm,
    CustomUserUpdateForm
)
from .models import Profile

# ثبت‌نام
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:dashboard")  # هدایت بعد از ثبت‌نام

    def form_valid(self, form):
        response = super().form_valid(form)
        # پاک کردن session قبلی قبل از login
        self.request.session.flush()
        # Login خودکار بعد ثبت‌نام با backend پیش‌فرض
        login(self.request, self.object, backend='django.contrib.auth.backends.ModelBackend')
        return response

# ورود کاربر
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "accounts/login.html"
    redirect_authenticated_user = True  # اگر کاربر لاگین باشد مستقیم هدایت شود

    def form_valid(self, form):
        # پاک کردن session قبلی قبل از login
        self.request.session.flush()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("accounts:dashboard")  # مسیر بعد از لاگین موفق

# خروج از سایت
class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        request.session.flush()
        return redirect("accounts:login")

    def post(self, request, *args, **kwargs):
        logout(request)
        request.session.flush()
        return redirect("accounts:login")

# ویرایش پروفایل
class ProfileUpdateView(LoginRequiredMixin, View):
    template_name = "accounts/edit_profile.html"

    def get(self, request, *args, **kwargs):
        user_form = CustomUserUpdateForm(instance=request.user)
        profile, _ = Profile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(instance=profile)
        return render(request, self.template_name, {
            "user_form": user_form,
            "profile_form": profile_form
        })

    def post(self, request, *args, **kwargs):
        user_form = CustomUserUpdateForm(request.POST, instance=request.user)
        profile, _ = Profile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("accounts:dashboard")

        return render(request, self.template_name, {
            "user_form": user_form,
            "profile_form": profile_form
        })

# داشبورد
def dashboard(request):
    return render(request, "accounts/dashboard.html")
