from django.contrib import admin

from apps.education.models.educational_institution import EducationalInstitution


@admin.register(EducationalInstitution)
class EducationalInstitutionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "institution_type",
    )
