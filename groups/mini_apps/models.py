from django.utils.translation import gettext_lazy as _

from django.db import models
from django.db.models import JSONField
from enum import Enum
from django.contrib.auth import get_user_model
User = get_user_model()

class MiniAppType(Enum):
    TYPE_A = 'Order'
    TYPE_B = 'Queue'

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class MiniApps(models.Model):
    """
    Default custom user model for Groups.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    name = models.CharField(_("Name of App"), blank=True, max_length=255)

    admins = models.ManyToManyField(User, related_name='admin_mini_apps')

    modified_at = models.DateTimeField()
    created_at = models.DateTimeField()

    app_type = models.CharField(max_length=50, choices=MiniAppType.choices())
    config = JSONField()

    deleted = models.BooleanField(default=False)
