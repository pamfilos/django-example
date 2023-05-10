from django.contrib import admin
from .models import Group

from django import forms
from ..mini_apps.models import MiniApps

from django.contrib.auth import get_user_model

User = get_user_model()


class GroupAdminForm(forms.ModelForm):
    messages = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        blank=True,
    )

    mini_apps = forms.ModelMultipleChoiceField(
        queryset=MiniApps.objects.all(),
        required=False,
        blank=True,
    )

    class Meta:
        model = Group
        fields = "__all__"


class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm


admin.site.register(Group, GroupAdmin)
