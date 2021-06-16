# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# App
from .models import User, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('displayname', 'photo')

    search_fields = (
        'user__email',
        'displayname',   
        'user__first_name',
        'user__last_name',
    )

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'updated',
    )

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'displayname', 'is_public', 'bio'),),
        }),
        ('Extra info', {
            'fields': (('updated', 'location', 'photo'),),
        })
    )

    readonly_fields = ('updated',)

class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""
    model = User
    list_display = (
        'email', 
        'is_staff', 
        'is_active',)
    list_filter = (
        'email', 
        'is_staff', 
        'is_active',)
    fieldsets = (
        ('User', {
            'fields': ('email', 'password')
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    inlines = (ProfileInline,)



admin.site.register(User, UserAdmin)
