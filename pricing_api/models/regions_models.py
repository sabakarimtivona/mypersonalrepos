from django.db import models
from django.contrib.postgres.fields import ArrayField

from .base_models import BaseModel

class Region(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    display_name = models.CharField(max_length=255)
    availability_zones = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    is_government = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['display_name']
