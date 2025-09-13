from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام لوله")
    image = models.ImageField(upload_to="products/", verbose_name="تصویر محصول")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات کوتاه")

    def __str__(self):
        return self.name
