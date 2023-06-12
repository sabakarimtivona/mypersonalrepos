from django.urls import path
from pricing_api import reg_price_views
from . import regions_views, vm_pp_views, vm_tier_views, vm_sku_views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    #path('', reg_price_views.PricingList.as_view()),
    path('regions', regions_views.RegionView.as_view()) ,
    path('regions/<str:region>', regions_views.RegionDetailView.as_view()) ,
    path('pricing_plans', vm_pp_views.VmPricingPlans.as_view()),
    path('vm_tiers', vm_tier_views.virtual_machine_tier.as_view()),
    path('skudetail/',vm_sku_views.VmSkuView.as_view()),
    path('skudetail/<str:sku>/<str:location>', vm_sku_views.VmSkuDetailView.as_view())


]

urlpatterns = format_suffix_patterns(urlpatterns)

