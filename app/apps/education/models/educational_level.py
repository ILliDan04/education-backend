from django.db import models
from extensions.django.db.models import AbstractUUIDModel


class EducationalLevel(AbstractUUIDModel):
    name = models.CharField()
    level = models.IntegerField()
