from django.db import models

# Create your models here.


class Issue(models.Model):
    issue_description = models.CharField(max_length=250, blank=False, default='')
    notes = models.CharField(max_length=400, blank=False, default='')
    issue_create_date = models.DateField()
    issue_due_date = models.DateField()
    program_id = models.CharField(max_length=200, blank=False, default='')
