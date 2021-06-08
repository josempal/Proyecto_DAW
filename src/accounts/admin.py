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
            'fields': (('user', 'photo', 'displayname', 'is_public', 'bio'),),
        }),
        ('Extra info', {
            'fields': (('updated'),),
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

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
