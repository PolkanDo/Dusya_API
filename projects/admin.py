from django.contrib import admin

from . import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'project_name',
        'project_owner',
        'project_field',
        'project_pub_date',
    ]
    list_filter = [
        'id',
        'project_name',
        'project_owner',
        'project_field',
        'project_pub_date',
    ]
