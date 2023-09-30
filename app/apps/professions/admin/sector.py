from django.contrib import admin
from apps.professions.models.sector import Sector


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('name',)
