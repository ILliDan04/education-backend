from apps.education.models import EducationalInstitutionType
from django.contrib import admin


@admin.register(EducationalInstitutionType)
class EducationalInstitutionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "required_educational_level",
        "education_level_on_graduation",
    )
