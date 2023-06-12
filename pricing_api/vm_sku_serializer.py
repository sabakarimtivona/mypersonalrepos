from rest_framework import serializers
from pricing_api.models.vm_sku_models import VmSizes , Pricing
from pricing_api.models.vm_benchmark_models import Benchmark
# from rest_framework.response import Response

class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = "__all__"
class BenchMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benchmark
        exclude = ['vmbenchRelation']

class VmSkuListSerializer(serializers.ModelSerializer) :
    pricing = PricingSerializer(many=True)
    Benchmark = BenchMarkSerializer(many=True)

    class Meta:
        model = VmSizes
        fields = ["vm_sku_name","vm_sku_details","family","vCPUs","MemoryGB","location","pricing","Benchmark"]     

