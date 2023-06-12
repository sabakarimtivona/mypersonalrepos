from django.shortcuts import render
from pricing_api.models.vm_sku_models import Pricing
from pricing_api.reg_price_serializers import PricingSerializer
from rest_framework import generics

# Create your views here.

class PricingList(generics.ListAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer