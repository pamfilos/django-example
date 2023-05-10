from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "groups.base_messages"
    verbose_name = _("Base Messages")
