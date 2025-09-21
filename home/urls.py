from django.urls import path
from .views import HomeView, AboutView, SubmitConsultationView

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='main'),
    path('about/', AboutView.as_view(), name='about'),
    path('catalog/', AboutView.as_view(), name='catalog'),
    path('submit-consultation/', SubmitConsultationView.as_view(), name='submit_consultation'),
]


