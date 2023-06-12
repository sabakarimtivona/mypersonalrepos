from rest_framework import generics
from pricing_api.models.vm_pp_models import VmPricingPlan
from .vm_pp_serializers import VmPricingPlanSerializer

class VmPricingPlans(generics.ListAPIView):
    queryset = VmPricingPlan.objects.all()
    serializer_class = VmPricingPlanSerializer
