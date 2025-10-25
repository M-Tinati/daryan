from django.db import models

class Product(models.Model):
    PE_CHOICES = [
        ("PE80", "PE80"),
        ("PE100", "PE100"),
    ]

    name = models.CharField(max_length=200, verbose_name="نام محصول")
    image = models.ImageField(upload_to="products/", verbose_name="تصویر محصول")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات کوتاه")

    size = models.IntegerField(
        verbose_name="سایز لوله/اینچ",
    )
    pressure = models.DecimalField(
        verbose_name="بار",
        max_digits=5,
        decimal_places=1,
        default=6.0
    )
    pe_type = models.CharField(max_length=10, choices=PE_CHOICES, verbose_name="نوع پلی‌اتیلن", default="PE100")

    def __str__(self):
        return self.name
