from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "groups.mini_apps"
    verbose_name = _("MiniApps")
