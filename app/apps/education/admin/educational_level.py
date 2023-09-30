from apps.education.models import EducationalLevel
from django.contrib import admin


@admin.register(EducationalLevel)
class EducationalLevelAdmin(admin.ModelAdmin):
    list_display = ("name", "level")
