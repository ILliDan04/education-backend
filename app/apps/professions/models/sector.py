from extensions.django.db.models import AbstractUUIDModel
from django.db import models


class Sector(AbstractUUIDModel):
    name = models.CharField(max_length=255, unique=True)
