from django.db import models

class Product(models.Model):
    PE_CHOICES = [
        ("PE80", "PE80"),
        ("PE100", "PE100"),
    ]

    name = models.CharField(max_length=200, verbose_name="نام محصول")
    image = models.ImageField(upload_to="products/", verbose_name="تصویر محصول")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات کوتاه")

    size = models.CharField(max_length=50, verbose_name="سایز لوله/اینچ")  # بدون choices
    pressure = models.PositiveIntegerField(verbose_name="بار", default=6)  # پیش‌فرض 6
    pe_type = models.CharField(max_length=10, choices=PE_CHOICES, verbose_name="نوع پلی‌اتیلن", default="PE100")

    def __str__(self):
        return self.name
