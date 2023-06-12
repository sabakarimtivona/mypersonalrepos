from pricing_api.models.regions_models import Region
from pricing_api.regions_serializer import RegionListSerializer
from rest_framework import generics

class RegionView(generics.ListAPIView): 
    queryset = Region.objects.all()
    serializer_class = RegionListSerializer

class RegionDetailView(generics.ListAPIView): 
    serializer_class = RegionListSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            region_name = self.kwargs.get('region')
            if region_name is not None:
                queryset = Region.objects.filter(name=region_name)
            return queryset