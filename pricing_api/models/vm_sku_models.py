"""
the model class for vm sku details .
"""
from django.db import models
from .base_models import BaseModel

class VmSizes(BaseModel):
    vm_sku_name = models.CharField(max_length=200)
    vm_sku_details = models.JSONField()
    family = models.CharField(max_length=200)
    vCPUs = models.IntegerField()
    MemoryGB = models.FloatField(default=0)
    location = models.CharField(max_length=200,default="")

class Pricing(BaseModel):
    currencyCode = models.CharField(max_length=100, blank=True, default='')
    tierMinimumUnits = models.FloatField()
    retailPrice = models.FloatField()
    unitPrice = models.FloatField()
    armRegionName = models.CharField(max_length=100, blank=True, default='')
    location = models.CharField(max_length=100, blank=True, default='')
    effectiveStartDate = models.CharField(max_length=100, blank=True, default='')
    meterId = models.CharField(max_length=100, blank=True, default='')
    meterName = models.CharField(max_length=100, blank=True, default='')
    productId = models.CharField(max_length=100, blank=True, default='')
    skuId = models.CharField(max_length=100, blank=True, default='')
    productName = models.CharField(max_length=100, blank=True, default='')
    skuName = models.CharField(max_length=100, blank=True, default='')
    serviceName = models.CharField(max_length=100, blank=True, default='')
    serviceId = models.CharField(max_length=100, blank=True, default='')
    serviceFamily = models.CharField(max_length=100, blank=True, default='')
    unitOfMeasure = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(max_length=100, blank=True, default='')
    isPrimaryMeterRegion = models.CharField(max_length=100, blank=True, default='')
    armSkuName = models.CharField(max_length=100, blank=True, default='')
    vmsize = models.ForeignKey(VmSizes, on_delete=models.CASCADE, related_name= "pricing",null=True, blank=True)


    

