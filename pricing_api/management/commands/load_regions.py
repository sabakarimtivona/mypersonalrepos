from typing import Dict

from django.core.management.base import BaseCommand
from pricing_api.models.regions_models import Region
from pricing_api.data_collection import locations

class Command(BaseCommand):
    help = "Data migrate into the DB"

    def handle(self, *args, **options):
        self.load_regions_data()

    def load_regions_data(self):
        """
        Load the region data into the Postgres
        :return: None
        """

        availability_zones = locations.availability_zones
        location_display_names = locations.location_display_names
        print("Started migrating data to the postgresDB")

        for location in availability_zones:
            if location in location_display_names:
                Region.objects.update_or_create(name=location, display_name=location_display_names[location], availability_zones=availability_zones[location], is_government=False)
        
        print("Data migration completed")

