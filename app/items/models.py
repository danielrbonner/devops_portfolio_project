from django.db import models
from bundles.models import Bundle

# Create your models here.


class Item(models.Model):
    item_description = models.CharField(
        max_length=250, blank=False, default='')
    upc = models.CharField(max_length=200, blank=False, default='')
    language = models.CharField(max_length=200, blank=False, default='')
    bundles = models.ManyToManyField(Bundle)
