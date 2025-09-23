# price/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from shop.models import Product
from .models import ProductPrice

@receiver(post_save, sender=Product)
def create_product_price(sender, instance, created, **kwargs):
    if created:
        ProductPrice.objects.create(product=instance)
