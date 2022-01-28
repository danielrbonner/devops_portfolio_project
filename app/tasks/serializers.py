from rest_framework import serializers
from issues.models import Issue


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'task_description', 'assigned_user_id', 'task_create_date', 'task_due_date', 'complete_date', 'status')
