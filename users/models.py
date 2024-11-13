from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import Group as OriginalGroup
from .managers import CustomUserManager
from django.db.models.signals import pre_delete
from django.dispatch import receiver

username_validator = UnicodeUsernameValidator()

class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            "unique": "Ya existe un usuario con ese nombre de usuario.",
        },
    )

    groups = models.ManyToManyField(
        OriginalGroup,
        related_name='custom_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    @property
    def nombre_completo(self):
        try:
            return self.nombre_completo
        except:
            return self.email

    @staticmethod
    @receiver(pre_delete, sender='users.User')
    def safe_delete_usuario(sender, instance, **kwargs):
        instance.safe_delete = True
        instance.save()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class Group(OriginalGroup):
    class Meta:
        proxy = True
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"