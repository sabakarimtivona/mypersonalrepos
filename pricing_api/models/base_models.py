from django.db import models
import uuid
from django.utils import timezone

class BaseModel(models.Model):    
    created_at = models.DateTimeField('created date', default=timezone.now)
    updated_at = models.DateTimeField('updated date', auto_now=True, null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4 )

    class Meta:
        abstract = True  
