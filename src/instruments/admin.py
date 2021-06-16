from django.contrib import admin
from .models import Instrument, InstrumentUser
# Register your models here.
@admin.register(Instrument)
class ExperienceAdmin(admin.ModelAdmin):
    """Instrument admin."""

    list_display = ('name', 'description')


admin.site.register(InstrumentUser)