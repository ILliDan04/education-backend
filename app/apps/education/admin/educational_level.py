from django.contrib import admin

from apps.education.models import EducationalLevel


@admin.register(EducationalLevel)
class EducationalLevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
