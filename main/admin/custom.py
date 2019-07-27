from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.admin import AdminSite
from reversion.admin import VersionAdmin

from main.models.user import CustomUser


class CustomAdminSite(AdminSite):
    site_url = None


class VersionedUserAdmin(VersionAdmin, UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональная информация', {'fields': ('full_name', 'email')}),
        ('Права', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Даты', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'full_name', 'is_staff')
    search_fields = ('username', 'full_name', 'email')


class VersionedGroupAdmin(VersionAdmin, GroupAdmin):
    pass


admin_site = CustomAdminSite()

admin_site.register(CustomUser, VersionedUserAdmin)
admin_site.register(Group, VersionedGroupAdmin)
