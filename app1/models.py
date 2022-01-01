from django.db import models
from django.utils import timezone

# Create your models here.
class stores(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    opening_time = models.TimeField(default=None, blank=True, null=True)
    closing_time = models.TimeField(default=None, blank=True, null=True)
    # price = models.FloatField
    price_json = models.JSONField(default=None, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)
    
