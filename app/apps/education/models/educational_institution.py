from django.db import models
from extensions.django.db.models import AbstractUUIDModel


class EducationalInstitution(AbstractUUIDModel):
    name = models.CharField(max_length=255)
    institution_type = models.ForeignKey(
        "education.EducationalInstitutionType",
        related_name="institutions",
        on_delete=models.PROTECT,
    )
