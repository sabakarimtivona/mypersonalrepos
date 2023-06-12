
from rest_framework import generics
from pricing_api.models.vm_tier_models import VmTier
from .vm_tier_serializer import virtual_machine_tierSerializer

class virtual_machine_tier(generics.ListAPIView):
    queryset = VmTier.objects.all()
    serializer_class = virtual_machine_tierSerializer