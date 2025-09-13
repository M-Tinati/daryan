from django.urls import path
from . import views

app_name = "shop"   # اینجا namespace تعریف میشه

urlpatterns = [
    path("", views.product_list, name="product_list"),
]
