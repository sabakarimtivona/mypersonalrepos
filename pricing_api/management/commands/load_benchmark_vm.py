from pricing_api.models import VmSizes, Benchmark
from django.core.management.base import BaseCommand
from pricing_api.data_collection import benchmark_vm

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.load_benchmark_data()

    def load_benchmark_data(self):
        
        benchmark_data = benchmark_vm.skus_data
        vmsize_objects, benchmark_objects = dict(), dict()

        for obj in VmSizes.objects.all():
            if obj.vm_sku_name in vmsize_objects:
                vmsize_objects[obj.vm_sku_name].append(obj)
            else:
                vmsize_objects[obj.vm_sku_name] = [obj]


        for obj in Benchmark.objects.all():
            if obj.vm_sku_name in benchmark_objects:
                benchmark_objects[obj.vm_sku_name].append(obj)
            else:
                benchmark_objects[obj.vm_sku_name] = [obj]



        for sku_name in vmsize_objects:
            for vmsize_obj in vmsize_objects[sku_name]:
                if sku_name in benchmark_objects:
                    for benchmark_obj in benchmark_objects[sku_name]:
                        benchmark_obj.vmbenchRelation.add(vmsize_obj)