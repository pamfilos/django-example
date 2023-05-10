from rest_framework import serializers

from ..models import MiniApps

class MiniAppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniApps
        fields = ["name"]
