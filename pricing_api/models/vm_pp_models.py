from django.db import models
import uuid

class VmPricingPlan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    type = models.CharField(max_length=200)
    def __str__(self):
        return self.type
