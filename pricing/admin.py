# pricing/admin.py
from django.contrib import admin
from .models import PipePrice

@admin.register(PipePrice)
class PipePriceAdmin(admin.ModelAdmin):
    list_display = ("size", "pressure", "pe_type", "weight", "price_per_kg", "total_price_display")
    list_filter = ("size", "pressure", "pe_type")
    search_fields = ("size", "pe_type")

    # ستون محاسبه شده برای قیمت کل
    def total_price_display(self, obj):
        return obj.total_price()
    total_price_display.short_description = "قیمت کل (تومان)"
