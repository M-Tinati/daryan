from django.contrib import admin
from django.shortcuts import render
from django import forms
from .models import PipePrice

class UpdatePriceForm(forms.Form):
    new_price_per_kg = forms.IntegerField(
        label="قیمت جدید هر کیلوگرم (تومان)",
        min_value=0,
        widget=forms.NumberInput(attrs={'step': '1000'}),
        help_text="قیمت جدید برای همه لوله‌های انتخاب‌شده اعمال خواهد شد (به تومان، بدون اعشار)."
    )

@admin.register(PipePrice)
class PipePriceAdmin(admin.ModelAdmin):
    list_display = ("size", "pressure", "pe_type", "weight_display", "price_per_kg_display", "total_price_display")
    list_filter = ("size", "pressure", "pe_type")
    search_fields = ("size", "pe_type")
    actions = ["update_price_per_kg"]

    # نمایش وزن به صورت کامل
    def weight_display(self, obj):
        return str(obj.weight)
    weight_display.short_description = "وزن لوله (کیلوگرم)"

    # نمایش قیمت هر کیلوگرم با فرمت تومان و بدون اعشار
    def price_per_kg_display(self, obj):
        return f"{int(obj.price_per_kg):,} تومان"
    price_per_kg_display.short_description = "قیمت هر کیلوگرم"

    # ستون محاسبه‌شده برای قیمت کل
    def total_price_display(self, obj):
        return f"{int(obj.total_price()):,} تومان"
    total_price_display.short_description = "قیمت کل"

    # اکشن برای به‌روزرسانی قیمت هر کیلوگرم
    def update_price_per_kg(self, request, queryset):
        if 'apply' in request.POST:
            form = UpdatePriceForm(request.POST)
            if form.is_valid():
                new_price = form.cleaned_data['new_price_per_kg']
                updated = queryset.update(price_per_kg=new_price)
                self.message_user(request, f"قیمت هر کیلوگرم برای {updated} لوله با موفقیت به {new_price:,} تومان به‌روزرسانی شد.")
                return
        else:
            form = UpdatePriceForm()

        return render(request, 'admin/update_price_form.html', {
            'title': 'به‌روزرسانی قیمت هر کیلوگرم',
            'form': form,
            'queryset': queryset,
            'action': 'update_price_per_kg',
            'opts': self.model._meta,
        })

    update_price_per_kg.short_description = "به‌روزرسانی قیمت هر کیلوگرم برای لوله‌های انتخاب‌شده"