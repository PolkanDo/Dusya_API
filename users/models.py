from django.contrib.auth.models import AbstractBaseUser, \
    BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):

    def create_user(self, email, first_name, last_name,
                    password, **other_fields):

        if not email:
            raise ValueError(_("You must provide an email address."))

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name,
                          last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password):
        pass


class User(AbstractBaseUser, PermissionsMixin):
    ROLES = (
        ("Seller", "Менеджер по продажам"),
        ("Head of sales", "Глава отдела продаж"),
        ("Integrator", "Интегратор"),
    )
    email = models.EmailField(
        'Email', db_index=True, unique=True, max_length=254,
        error_messages={'required': _('Field must be filled.'),
                        'unique': _('A user with this email '
                                    'is already registered ')})
    first_name = models.CharField(_('First name'), max_length=150)
    last_name = models.CharField(_('Last name'), max_length=150)
    role = models.CharField(max_length=1, choices=ROLES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    class Meta:
        ordering = ['-id']
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.get_full_name()
