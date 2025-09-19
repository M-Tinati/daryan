from django.db import models
from django.conf import settings
from shop.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'در انتظار بررسی'),
        ('confirmed', 'تایید شده'),
        ('shipped', 'ارسال شده'),
        ('completed', 'اتمام یافته'),
        ('canceled', 'لغو شده'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name="کاربر"
    )
    full_name = models.CharField(max_length=200, verbose_name="نام و نام خانوادگی", default="")
    phone = models.CharField(max_length=11, verbose_name="شماره تلفن", default="")
    national_id = models.CharField(max_length=10, verbose_name="کد ملی", default="")
    address = models.TextField(blank=True, null=True, verbose_name="آدرس کامل", default="")
    national_code = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین تغییر")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name="وضعیت سفارش"
    )

    def __str__(self):
        return f"سفارش #{self.id} توسط {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="سفارش"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="order_items",
        verbose_name="محصول"
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="تعداد")
    length = models.PositiveIntegerField(default=0, verbose_name="متراژ")


    def __str__(self):
        return f"{self.quantity} × {self.product.name}"
