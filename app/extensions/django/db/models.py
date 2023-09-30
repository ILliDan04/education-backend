from uuid import uuid4

from django.db import models


class AbstractUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta(models.base.ModelBase):
        abstract = True


class AbstractTimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(models.base.ModelBase):
        abstract = True
