from django.contrib import admin
from .models import MiniApps


class MiniAppsAdmin(admin.ModelAdmin):
    pass

admin.site.register(MiniApps, MiniAppsAdmin)