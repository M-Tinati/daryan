from django.urls import path
from .views import CreateOrderView, MyOrdersView

app_name = 'orders'

urlpatterns = [
    path('create/<int:product_id>/', CreateOrderView.as_view(), name='create_order'),
    path('my-orders/', MyOrdersView.as_view(), name='my_orders'),
]
