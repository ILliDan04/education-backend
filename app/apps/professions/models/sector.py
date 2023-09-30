from django.db import models
from extensions.django.db.models import AbstractUUIDModel


class Sector(AbstractUUIDModel):
    name = models.CharField(max_length=255, unique=True)
