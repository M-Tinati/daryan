from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PipePrice
from shop.models import Product  # اگر نیاز داری با Product کار کنی

@receiver(post_save, sender=PipePrice)
def update_product_price(sender, instance, **kwargs):
    """وقتی قیمت لوله تغییر کرد، قیمت محصول متناظر را هم آپدیت کن"""
    if instance.product:
        # اگر مدل Product خودش فیلد قیمت دارد
        if hasattr(instance.product, "price_value"):
            instance.product.price_value = instance.total_price()
            instance.product.save()
