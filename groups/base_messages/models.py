from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from groups.users.managers import UserManager
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class BaseMessages(models.Model):
    """
    Default custom user model for Groups.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    content = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE, related_name='base_messages')
    sent_at = models.DateTimeField(auto_now_add=True)