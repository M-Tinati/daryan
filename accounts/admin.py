from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    # ستون‌هایی که توی لیست کاربران نمایش داده میشن
    list_display = ("username", "first_name", "last_name", "phone", "city", "is_staff", "is_active")
    
    # قابلیت جستجو
    search_fields = ("username", "first_name", "last_name", "phone", "city")
    
    # مرتب‌سازی
    ordering = ("phone",)
    
    # فیلدهایی که توی فرم تغییر اطلاعات کاربر نشون داده میشن
    fieldsets = (
        (None, {"fields": ("phone", "username", "password")}),
        ("اطلاعات شخصی", {"fields": ("first_name", "last_name", "city")}),
        ("دسترسی‌ها", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )

    # فیلدهایی که توی فرم اضافه کردن کاربر جدید هست
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("phone", "username", "password1", "password2", "first_name", "last_name", "city", "is_staff", "is_active"),
        }),
    )
