from django.contrib import admin
from .models import Product
from price.models import ProductPrice

class ProductPriceInline(admin.StackedInline):
    model = ProductPrice
    extra = 0
    min_num = 1
    max_num = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "size", "pressure", "pe_type", "get_price")
    list_filter = ("pressure", "pe_type")
    search_fields = ("name", "size")
    inlines = [ProductPriceInline]

    def get_price(self, obj):
        if hasattr(obj, 'price') and obj.price.price:
            return f"{obj.price.price:,} تومان"  # عدد با جداکننده هزار و تومان
        return "-"
    get_price.short_description = "قیمت"
