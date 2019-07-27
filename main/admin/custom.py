from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from reversion.admin import VersionAdmin

from main.models import CustomUser


class CustomAdminSite(AdminSite):
    site_url = None
    # Text to put at the end of each page's <title>.
    site_title = 'Мед+'

    # Text to put in each page's <h1>.
    site_header = 'Мед+'

    # Text to put at the top of the admin index page.
    index_title = 'Главная'


class VersionedUserAdmin(VersionAdmin, UserAdmin):
    # TODO: закинуть пациента
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
