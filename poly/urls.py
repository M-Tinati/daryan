from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static   # برای سرو فایل‌های media

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('products/', include(('shop.urls', 'shop'), namespace='shop')),
    path('orders/', include('orders.urls', namespace='orders')),

]

if settings.DEBUG:  # فقط وقتی DEBUG=True باشه (یعنی در حالت توسعه)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
