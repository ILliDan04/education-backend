from django.db import models
from extensions.django.db.models import AbstractUUIDModel


class Profession(AbstractUUIDModel):
    name = models.CharField(max_length=255, unique=True)
    sector = models.ForeignKey(
        "professions.Sector",
        related_name="professions",
        on_delete=models.CASCADE,
        null=True,
    )
