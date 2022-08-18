from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdminConfig(UserAdmin):
    search_fields = ("email", "role", "first_name", "last_name")
    list_filter = ("email", "role", "first_name", "last_name",
                   "is_active", "is_staff")
    ordering = ("-last_name", "-role")
    list_display = ("email", "role", "first_name", "last_name",
                    "is_active", "is_staff")
    fieldsets = (
        (None, {"fields": ("email",)}),
        ("Personal", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("role", "is_staff", "is_active")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "role",
                       "password1", "password2", "is_active", "is_staff"),
        }),
    )


admin.site.register(User, UserAdminConfig)
