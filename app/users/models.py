from django.db import models

class User(models.Model):
    email = models.CharField(max_length=250, blank=False, default='')
    first_name = models.CharField(max_length=250, blank=False, default='')
    last_name = models.CharField(max_length=250, blank=False, default='')
    password = models.CharField(max_length=250, blank=False, default='')
    