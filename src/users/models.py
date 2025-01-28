import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField(
        "Email",
        unique=True,
        error_messages={"unique": "Пользователь с таким email уже существует"},
    )
    first_name = models.CharField(verbose_name="first name", max_length=150, blank=True)
    last_name = models.CharField(verbose_name="last name", max_length=150, blank=True)
    is_staff = models.BooleanField(verbose_name="staff status", default=False)
    is_active = models.BooleanField("active", default=True)
    photo = models.ImageField(
        verbose_name="Фото",
        upload_to="users/photos/",
        blank=True,
    )
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата последнего обновления", auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        db_table = "users"

    def __str__(self) -> str:
        return self.email
