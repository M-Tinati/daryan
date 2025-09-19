from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class PhoneBackend(ModelBackend):
    """
    Backend برای کاربران معمولی با شماره تلفن.
    ادمین از backend پیش‌فرض Django استفاده می‌کند.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(phone=username)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None
