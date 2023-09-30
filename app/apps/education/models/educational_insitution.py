from django.db import models
from extensions.django.db.models import AbstractUUIDModel


class EducationalInstitution(AbstractUUIDModel):
    name = models.CharField(max_length=255)
    required_educational_level = models.ForeignKey(
        "education.EducationalLevel",
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
    )
    education_level_on_graduation = models.ForeignKey(
        "education.EducationalLevel",
        related_name="educational_institutions",
        on_delete=models.CASCADE,
        null=True,
    )
