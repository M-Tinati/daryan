from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.conf import settings

class CustomUserManager(BaseUserManager):
    def create_user(self, phone, username, password=None, **extra_fields):
        if not phone:
            raise ValueError("شماره تلفن الزامی است")
        user = self.model(phone=phone, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone, username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=11, unique=True, verbose_name="شماره تلفن")
    username = models.CharField(max_length=50, unique=True, verbose_name="نام کاربری")
    first_name = models.CharField(max_length=30, blank=True, null=True, verbose_name="نام")
    last_name = models.CharField(max_length=30, blank=True, null=True, verbose_name="نام خانوادگی")

    CITY_CHOICES = [
        ("تبریز", "تبریز"),
        ("مراغه", "مراغه"),
        ("مرند", "مرند"),
        ("اهر", "اهر"),
        ("بناب", "بناب"),
        ("میانه", "میانه"),
        ("شبستر", "شبستر"),
        ("هشترود", "هشترود"),
        ("سراب", "سراب"),
        ("آذرشهر", "آذرشهر"),
        ("اسکو", "اسکو"),
        ("بستان‌آباد", "بستان‌آباد"),
    ]
    city = models.CharField(max_length=30, choices=CITY_CHOICES, blank=True, null=True, verbose_name="شهر")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.username} ({self.phone})"

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    address = models.TextField(blank=True, null=True, verbose_name="آدرس کامل")

    def __str__(self):
        return f"{self.user.username} Profile"

class UserFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to='user_files/')
    description = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} - {self.user.username}"
