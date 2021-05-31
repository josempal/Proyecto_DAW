from django.contrib import admin
from .models import Instrument
# Register your models here.
@admin.register(Instrument)
class ExperienceAdmin(admin.ModelAdmin):
    """Instrument admin."""

    list_display = ('name', 'description')