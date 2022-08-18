from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdminConfig(UserAdmin):

    ordering = ("-last_name",)
    list_display = ("email", "first_name", "last_name",
                    "is_active", "is_staff")


admin.site.register(User, UserAdminConfig)
