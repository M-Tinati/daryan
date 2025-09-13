from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login , logout
from django.views import View

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:dashboard")  # هدایت بعد از ثبت‌نام

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # لاگین خودکار بعد ثبت‌نام
        return response

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "accounts/login.html"
    redirect_authenticated_user = True  # اگر کاربر لاگین باشد مستقیم هدایت شود

    def get_success_url(self):
        return reverse_lazy("accounts:dashboard")  # مسیر بعد از لاگین موفق


class CustomLogoutView(View):
    def get(self, request):
        logout(request)  # حذف session و لاگین کاربر
        return redirect("accounts:login")