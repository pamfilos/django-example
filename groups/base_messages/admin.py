from django.contrib import admin
from .models import BaseMessages

from django import forms
from ..groups.models import Group

class BaseMessagesAdmin(admin.ModelAdmin):
    pass
    # group = forms.ModelFormOptions(
    #     queryset=Group.objects.all(),
    #     widget=forms.ChoiceField,
    #     required=False,
    #            blank=True,
    # )


admin.site.register(BaseMessages, BaseMessagesAdmin)