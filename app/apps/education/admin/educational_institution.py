from apps.education.models import EducationalInstitution
from django.contrib import admin


@admin.register(EducationalInstitution)
class EducationalInstitutionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "required_educational_level",
        "education_level_on_graduation",
    )
