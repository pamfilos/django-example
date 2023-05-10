from rest_framework import serializers

from ..models import Group
from groups.users.api.serializers import UserSerializer

class GroupSerializer(serializers.ModelSerializer):
    subscribers = UserSerializer(many=True)
    admins = UserSerializer(many=True)
    class Meta:
        model = Group
        fields = ["name", "subscribers", "admins"]

