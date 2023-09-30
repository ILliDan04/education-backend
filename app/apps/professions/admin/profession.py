from apps.professions.models.profession import Profession
from django.contrib import admin


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ("name", "sector")
