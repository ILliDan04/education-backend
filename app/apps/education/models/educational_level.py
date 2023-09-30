from extensions.django.db.models import AbstractUUIDModel
from django.db import models


class EducationalLevel(AbstractUUIDModel):
    name = models.CharField()
    level = models.IntegerField()
