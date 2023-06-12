from django.db import models
import uuid
from django.utils import timezone
class VmTier(models.Model):
    tier = models.CharField(max_length=200)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.tier
