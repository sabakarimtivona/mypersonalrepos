from rest_framework import serializers
from pricing_api.models.vm_tier_models import VmTier

class virtual_machine_tierSerializer(serializers.ModelSerializer):
     class Meta:
        model = VmTier
        fields = [ 'id' ,'tier']
