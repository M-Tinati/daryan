# pricing/urls.py
from django.urls import path
from .views import PriceInquiryView

app_name = "pricing"

urlpatterns = [
    path("price-inquiry/", PriceInquiryView.as_view(), name="price_inquiry"),
]
