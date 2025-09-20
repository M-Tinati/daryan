from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()

    # دریافت پارامترهای فیلتر از GET
    size = request.GET.get("size")
    if size:
        products = products.filter(size=size)

    pressure = request.GET.get("pressure")
    if pressure:
        products = products.filter(pressure=pressure)

    pe_type = request.GET.get("pe_type")
    if pe_type:
        products = products.filter(pe_type=pe_type)

    products = products.order_by("-id")

    # مقادیر یکتا برای تولید فیلترهای کشویی دینامیک
    sizes = Product.objects.values_list('size', flat=True).distinct()
    pressures = Product.objects.values_list('pressure', flat=True).distinct()
    pe_types = Product.objects.values_list('pe_type', flat=True).distinct()

    context = {
        "products": products,
        "sizes": sizes,
        "pressures": pressures,
        "pe_types": pe_types,
        "selected_size": size,
        "selected_pressure": pressure,
        "selected_pe_type": pe_type,
    }

    return render(request, "shop/product_list.html", context)
