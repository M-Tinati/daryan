# filename: shop/admin.py
from django.contrib import admin
from .models import Product
from price.models import PipePrice  # ✅ اصلاح شد

class PipePriceInline(admin.StackedInline):
    model = PipePrice
    extra = 0
    min_num = 1
    max_num = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "size", "pressure", "pe_type", "get_price")
    list_filter = ("pressure", "pe_type")
    search_fields = ("name", "size")
    inlines = [PipePriceInline]  # ✅ حالا از PipePrice استفاده می‌کنیم

    def get_price(self, obj):
        if hasattr(obj, 'price') and obj.price:
            return f"{obj.price.total_price():,} تومان"  # ✅ محاسبه از PipePrice
        return "-"
    get_price.short_description = "قیمت کل"
