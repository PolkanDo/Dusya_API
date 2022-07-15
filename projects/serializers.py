from .models import Project
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'project_id',
            'project_name',
            'project_owner',
            'project_field',
            'project_pub_date',
        )
