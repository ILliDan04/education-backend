from django.contrib import admin

from apps.professions.models.profession import Profession


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'sector')
