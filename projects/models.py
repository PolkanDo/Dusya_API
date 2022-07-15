from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Project(models.Model):
    project_id = models.AutoField(primery_key=True)
    project_name = models.CharField(
        max_length=250,
        verbose_name="Project Name",
        unique=True
    )
    project_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Project Author',
        related_name='projects',
    )
    project_field = models.CharField(
        verbose_name="Project Description"
    )
    project_pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Publication_date'
    )

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-pub_date']

    def __str__(self):
        return f'Project: {self.project_name}'

