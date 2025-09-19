# orders/views.py
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import FormView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.urls import reverse_lazy

from shop.models import Product
from .models import Order, OrderItem

# فرم ثبت سفارش
class OrderCreateForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        label="تعداد",
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    length = forms.DecimalField(
        min_value=0,
        label="متراژ (متر)",
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    address = forms.CharField(
        label="آدرس",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3})
    )
    full_name = forms.CharField(
        label="نام و نام خانوادگی",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    phone = forms.CharField(
        label="شماره تلفن",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    national_code = forms.CharField(
        label="کد ملی",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

# ویو ثبت سفارش
class CreateOrderView(LoginRequiredMixin, FormView):
    template_name = "orders/create_order.html"
    form_class = OrderCreateForm

    def dispatch(self, request, *args, **kwargs):
        # محصول مورد نظر
        self.product = get_object_or_404(Product, id=kwargs.get("product_id"))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # ایجاد سفارش
        order = Order.objects.create(
            user=self.request.user,
            full_name=form.cleaned_data["full_name"],
            phone=form.cleaned_data["phone"],
            address=form.cleaned_data["address"],
            national_code=form.cleaned_data["national_code"],
            status="pending",
        )

        # اضافه کردن آیتم سفارش
        OrderItem.objects.create(
            order=order,
            product=self.product,
            quantity=form.cleaned_data["quantity"],
            length=form.cleaned_data["length"]
        )

        return redirect("orders:my_orders")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = self.product
        return context

# ویو لیست سفارش‌های کاربر
class MyOrdersView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "orders/my_orders.html"
    context_object_name = "orders"

    def get_queryset(self):
        # فقط سفارش‌های کاربر فعلی
        return Order.objects.filter(user=self.request.user).order_by("-created_at")
