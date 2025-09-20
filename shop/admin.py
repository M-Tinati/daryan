from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "size", "pressure", "pe_type")
    list_filter = ("pressure", "pe_type")  # سایز در لیست فیلتر نمی‌گذاریم چون نامحدود است
    search_fields = ("name", "size")
