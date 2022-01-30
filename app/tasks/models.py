from django.db import models
from users.models import User


# Create your models here.

class Task(models.Model):
    task_description = models.CharField(max_length=250, blank=False, default='')
    assigned_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    task_create_date = models.DateField()
    task_due_date = models.DateField()
    complete_date = models.DateField()
    status = models.CharField(max_length=200, blank=False, default='')
