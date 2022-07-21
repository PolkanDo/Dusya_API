from django.contrib import admin

from . import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'project_type',
        'project_author',
        'project_start_date',
        'project_completion_date',
        'project_executor',
    ]
    list_filter = [
        'id',
        'project_type',
        'project_author',
        'project_start_date',
        'project_completion_date',
        'project_executor',
    ]
