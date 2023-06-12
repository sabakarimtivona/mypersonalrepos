from django.db import models
from .base_models import BaseModel
from .vm_sku_models import VmSizes

class Benchmark(BaseModel):
    vm_sku_name= models.CharField(max_length=250)
    operating_system = models.CharField(max_length=200)
    CPU = models.CharField(max_length=200)
    vCPUs = models.CharField(max_length=200) 
    NUMA_Nodes = models.CharField(max_length=200) 
    Memory = models.CharField(max_length=200) 
    Avg_Score = models.CharField(max_length=200) 
    StdDev = models.CharField(max_length=200) 
    StdDev_percentage = models.CharField(max_length=200) 
    Runs = models.CharField(max_length=200)
    Published_date = models.CharField(max_length=200)

    vmbenchRelation = models.ManyToManyField(VmSizes, related_name='Benchmark')

    class Meta:
        ordering = ["vm_sku_name"]
        unique_together = ('vm_sku_name','operating_system','CPU','NUMA_Nodes')

    def __str__(self):
        return self.vm_sku_name