from .models import Project
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id',
            'project_type',
            'project_author',
            'project_start_date',
            'project_completion_date',
            'project_executor',
        )
