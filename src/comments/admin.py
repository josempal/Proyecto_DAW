from django.contrib import admin
from .models import Comment
# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Comment admin."""

    list_display = ('body', 'updated', 'creator', 'profile')