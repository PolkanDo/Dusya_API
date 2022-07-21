from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
"""
!!!
Изменить отображение type field, project author и project executor.
добавить комментарии и авторизацию.
!!!
"""


class ProjectType(models.Model):
    type = models.CharField(
        max_length=250, verbose_name="Project Name", unique=True
    )


class Project(models.Model):
    merchant_id = models.IntegerField(
        blank=False, null=False,
        validators=[MinValueValidator(1), MaxValueValidator(10000000)],
    )
    project_type = models.ForeignKey(
        ProjectType, on_delete=models.SET_NULL, verbose_name='Project Type',
        related_name='types', null=True
    )
    project_author = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name='Project Author',
        related_name='authors_projects', null=True
    )
    project_start_date = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name='Publication_date'
    )
    project_completion_date = models.DateTimeField(
        db_index=True, verbose_name='Completion date', null=True, blank=True
    )
    project_executor = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name='Project Executor',
        related_name='executors_projects', null=True,
    )
    project_description = models.CharField(
        max_length=1000, verbose_name="Project Description", blank=False,
    )

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-project_start_date']

    def __str__(self):
        return f'Project: {self.project_type}'
