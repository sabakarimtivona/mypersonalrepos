from rest_framework import serializers
from pricing_api.models.vm_sku_models import Pricing

class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = ['currencyCode','tierMinimumUnits','retailPrice','unitPrice','armRegionName','location','effectiveStartDate','meterId','meterName','productId','skuId','productName','skuName','serviceName','serviceId','serviceFamily','unitOfMeasure','type','isPrimaryMeterRegion','armSkuName']