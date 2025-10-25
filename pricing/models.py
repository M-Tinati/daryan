from django.db import models

class PipePrice(models.Model):
    PE_CHOICES = [
        ("PE80", "PE80"),
        ("PE100", "PE100"),
    ]

    size = models.IntegerField(
        verbose_name="سایز لوله/اینچ",
            # بسته به بزرگترین سایز
    )
    pressure = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        verbose_name="بار",
        default=6.0
    )
    pe_type = models.CharField(max_length=5, choices=PE_CHOICES, verbose_name="نوع PE")
    weight = models.FloatField(verbose_name="وزن لوله (کیلوگرم)", default=0.0)
    price_per_kg = models.IntegerField(verbose_name="قیمت هر کیلوگرم (تومان)", default=0)

    def __str__(self):
        return f"{self.size} - {self.pressure} بار - {self.pe_type}"

    def total_price(self):
        return int(self.weight * self.price_per_kg)
