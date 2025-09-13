from django.shortcuts import render
from django.views import View
from shop.models import Product
from blog.models import Post  # اضافه کردن مدل وبلاگ
from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .forms import ConsultationRequestForm

class HomeView(View):
    template_name = 'home/home.html'

    def get(self, request):
        # محصولات
        products = Product.objects.all()[:10]  # 10 محصول آخر

        # اخبار/وبلاگ
        posts = Post.objects.all().order_by('-created_at')[:3]  # 3 خبر آخر

        context = {
            'products': products,
            'posts': posts
        }
        return render(request, self.template_name, context)

    def post(self, request):
        pass
class AboutView(View):
    template_name = 'home/about.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        # دریافت داده‌های فرم
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # ارسال ایمیل (اختیاری)
        full_message = f"نام: {name}\nشماره تماس: {phone}\nایمیل: {email}\nموضوع: {subject}\nپیام: {message}"
        send_mail(
            subject=f"پیام تماس با ما: {subject}",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],
        )

        # نمایش پیام موفقیت
        return render(request, self.template_name, {"success": True})
# myapp/views.py
from django.views import View
from django.http import JsonResponse
from .models import ConsultationRequest

class SubmitConsultationView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # ذخیره در دیتابیس
        ConsultationRequest.objects.create(
            name=name,
            phone=phone,
            email=email,
            subject=subject,
            message=message
        )

        return JsonResponse({"success": True})

    def get(self, request, *args, **kwargs):
        # درخواست GET مجاز نیست
        return JsonResponse({"success": False}, status=400)
