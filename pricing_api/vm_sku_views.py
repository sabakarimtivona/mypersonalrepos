from pricing_api.vm_sku_serializer import VmSkuListSerializer
from rest_framework import generics
from pricing_api.models.vm_sku_models import VmSizes, Pricing
from pricing_api.models.vm_benchmark_models import Benchmark

class VmSkuView(generics.ListAPIView):
    queryset =  VmSizes.objects.all().prefetch_related('Benchmark','pricing')
    serializer_class = VmSkuListSerializer

class VmSkuDetailView(generics.ListAPIView):
    serializer_class = VmSkuListSerializer
    def get_queryset(self):
        if self.request.method == 'GET':
            VmSku_name = self.kwargs.get('sku')
            location = self.kwargs.get('location')
            if VmSku_name is not None:
                queryset = VmSizes.objects.filter(vm_sku_name=VmSku_name, location = location)
            return queryset