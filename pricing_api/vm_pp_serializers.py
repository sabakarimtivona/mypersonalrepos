from rest_framework import serializers
from pricing_api.models.vm_pp_models import VmPricingPlan

class VmPricingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = VmPricingPlan
        fields = ['id', 'type']