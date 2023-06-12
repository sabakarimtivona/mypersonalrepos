
from django.core.management.base import BaseCommand
from pricing_api.models.vm_sku_models import Pricing
from ...data_collection import regionalvmpricing

class Command(BaseCommand):
    help = "Data migrate into the DB"

    def handle(self, *args, **options):
        self.load_vm_price()

    def load_vm_price(self):
        """
        Load the vm price data into the Postgres
        """
        pricing_data = regionalvmpricing.execute_thread()
        Pricing.objects.bulk_create(pricing_data)
        print("Data migration completed")