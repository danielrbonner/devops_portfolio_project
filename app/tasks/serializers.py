from rest_framework import serializers
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'task_description', 'assigned_user_id', 'task_create_date', 'task_due_date', 'complete_date', 'status')
