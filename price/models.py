from django.db import models
from shop.models import Product

class ProductPrice(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="price")
    price = models.PositiveIntegerField(null=True, blank=True, verbose_name="قیمت (تومان)")

    def __str__(self):
        return f"{self.product.name} - {self.price if self.price else 'بدون قیمت'}"
