from rest_framework import serializers
from issues.models import Issue


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'issue_description', 'notes', 'issue_create_date', 'issue_due_date', 'program_id')
