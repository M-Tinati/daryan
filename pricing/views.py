# pricing/views.py
from django.views.generic import ListView
from .models import PipePrice

class PriceInquiryView(ListView):
    model = PipePrice
    template_name = "pricing/price_inquiry.html"
    context_object_name = "pipes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        weight_input = self.request.GET.get("weight", None)
        try:
            weight = float(weight_input) if weight_input else 0
        except ValueError:
            weight = 0
        context["weight"] = weight
        return context
