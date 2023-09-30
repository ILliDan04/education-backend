from django.contrib import admin

from apps.education.models import EducationalInstitution


@admin.register(EducationalInstitution)
class EducationalInstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'required_educational_level', 'education_level_on_graduation')
