from django.utils.translation import gettext_lazy as _

from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()


class Group(models.Model):
    """
    Default custom user model for Groups.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    group_id = models.CharField(max_length=255, unique=True)

    name = models.CharField(_("Name of Group"), blank=True, max_length=255)

    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    admins = models.ManyToManyField(User, related_name='admin_groups')
    subscribers = models.ManyToManyField(User, related_name='subscriber_groups')
    messages = models.ManyToManyField('base_messages.BaseMessages', related_name='base_message_groups')
    mini_apps = models.ManyToManyField('mini_apps.MiniApps', related_name='mini_apps_groups')

    deleted = models.BooleanField(default=False)
