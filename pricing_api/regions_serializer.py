from rest_framework import serializers
from pricing_api.models.regions_models import Region
from rest_framework.response import Response

class RegionListSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Region
        fields = ['id' , 'name' , 'display_name' , 'availability_zones' , 'is_government']  