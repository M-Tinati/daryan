# filename: pricing/views.py
from django.views.generic import ListView
from shop.models import Product  # از مدل Product می‌خوانیم

class PriceInquiryView(ListView):
    model = Product
    template_name = "pricing/price_inquiry.html"
    context_object_name = "pipes"  # برای سازگاری با قالب فعلی

    def get_queryset(self):
        """
        برمی‌گرداند تمام محصولات با داده‌های PipePrice مرتبط
        فقط محصولاتی که قیمت دارند نمایش داده می‌شوند
        """
        queryset = super().get_queryset().select_related("price")
        queryset = queryset.filter(price__isnull=False)
        return queryset

    def get_context_data(self, **kwargs):
        """افزودن داده‌های اضافی (مثل وزن ورودی کاربر، اگر خواستی)"""
        context = super().get_context_data(**kwargs)
        return context
