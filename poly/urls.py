from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('products/', include(('shop.urls', 'shop'), namespace='shop')),
    path('orders/', include('orders.urls', namespace='orders')),
    path("pricing/", include("pricing.urls", namespace="pricing")),
    path('i18n/', include('django.conf.urls.i18n')),  # ✅ اینجا اضافه شد
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
