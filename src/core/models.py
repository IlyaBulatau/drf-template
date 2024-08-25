import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(
        verbose_name="Активная запись", help_text="Активная запись", default=True
    )
    created_at = models.DateTimeField(
        verbose_name="Время создания", help_text="Время создания", auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Время последнего обновления",
        help_text="Время последнего обновления",
        auto_now=True,
    )

    class Meta:
        abstract = True
