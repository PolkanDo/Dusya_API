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

