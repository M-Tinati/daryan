from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile, UserFile

# Inline پروفایل
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "اطلاعات آدرس"

# Inline فایل کاربر
class UserFileInline(admin.TabularInline):
    model = UserFile
    extra = 1

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    list_display = ("username", "first_name", "last_name", "phone", "city", "is_staff", "is_active")
    search_fields = ("username", "first_name", "last_name", "phone", "city")
    ordering = ("phone",)
    
    fieldsets = (
        (None, {"fields": ("phone", "username", "password")}),
        ("اطلاعات شخصی", {"fields": ("first_name", "last_name", "city")}),
        ("دسترسی‌ها", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("phone", "username", "password1", "password2", "first_name", "last_name", "city", "is_staff", "is_active"),
        }),
    )

    inlines = (ProfileInline, UserFileInline)

    # محدود کردن queryset برای کاربران معمولی
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(id=request.user.id)
