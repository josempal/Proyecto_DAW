from django.contrib import admin
from .models import Experience
# Register your models here.
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """Experience admin."""

    list_display = ('type', 'duration', 'creator')