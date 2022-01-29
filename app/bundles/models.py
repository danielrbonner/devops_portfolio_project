from django.db import models
from programs.models import Program

# Create your models here.


class Bundle(models.Model):
    description = models.CharField(max_length=250, blank=False, default='')
    programs = models.ManyToManyField(Program)
    upc = models.CharField(max_length=200, blank=False, default='')
