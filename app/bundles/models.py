from django.db import models

# Create your models here.


class Bundle(models.Model):
    description = models.CharField(max_length=250, blank=False, default='')
    upc = models.CharField(max_length=200, blank=False, default='')
