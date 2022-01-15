from django.db import models

class Program(models.Model):
    program_id = models.CharField(max_length=20, blank=False, default='')
    program_name = models.CharField(max_length=200, blank=False, default='')
    program_type = models.CharField(max_length=50, blank=True, null=True)
    retailer = models.CharField(max_length=50, blank=True)
    retailer_item_nbr = models.CharField(max_length=20, blank=True)
    program_UPC = models.CharField(max_length=20, blank=True)
    season = models.CharField(max_length=20, blank=True)
    year = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20, blank=False, default='')
