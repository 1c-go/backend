from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.admin import AdminSite

from reversion.admin import VersionAdmin


class CustomAdminSite(AdminSite):
    site_url = None


class VersionedUserAdmin(VersionAdmin, UserAdmin):
    pass


class VersionedGroupAdmin(VersionAdmin, GroupAdmin):
    pass


admin_site = CustomAdminSite()

admin_site.register(User, VersionedUserAdmin)
admin_site.register(Group, VersionedGroupAdmin)
