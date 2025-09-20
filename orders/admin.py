from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Count
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id", 
        "user", 
        "user_order_count", 
        "item_count_colored", 
        "colored_status", 
        "created_at", 
        "order_items_summary"
    )
    list_filter = ("status", "created_at")
    search_fields = ("user__username", "id")
    inlines = [OrderItemInline]

    # annotate برای عملکرد بهتر و مرتب‌سازی
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(
            item_count=Count('items', distinct=True),
            user_order_count=Count('user__orders', distinct=True)
        )
        return qs

    # وضعیت رنگی با tooltip
    def colored_status(self, obj):
        color = {
            'pending': 'orange',
            'confirmed': 'blue',
            'shipped': 'purple',
            'completed': 'green',
            'canceled': 'red',
        }.get(obj.status, 'black')
        return format_html(
            '<b style="color: {}; cursor: help;" title="وضعیت واقعی: {}">{}</b>',
            color, obj.status, obj.get_status_display()
        )
    colored_status.short_description = "وضعیت"
    colored_status.admin_order_field = "status"

    # تعداد آیتم‌ها با رنگ
    def item_count_colored(self, obj):
        count = getattr(obj, "item_count", obj.items.count())
        color = "red" if count > 5 else "black"
        return format_html('<span style="color: {};" title="تعداد آیتم‌ها">{}</span>', color, count)
    item_count_colored.short_description = "تعداد آیتم‌ها"
    item_count_colored.admin_order_field = "item_count"

    # تعداد کل سفارش‌های کاربر
    def user_order_count(self, obj):
        count = getattr(obj, "user_order_count", Order.objects.filter(user=obj.user).count())
        return format_html('<span title="تعداد کل سفارش‌های کاربر">{}</span>', count)
    user_order_count.short_description = "تعداد سفارش‌های کاربر"
    user_order_count.admin_order_field = "user_order_count"

    # خلاصه محصولات هر سفارش
    def order_items_summary(self, obj):
        items = obj.items.all()
        if not items:
            return "-"
        summary = [f"{item.product.name} ({item.quantity})" for item in items]
        if len(summary) > 3:
            return format_html("{}…", ", ".join(summary[:3]))
        return ", ".join(summary)
    order_items_summary.short_description = "محصولات سفارش"
