from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import GroupSerializer
from ..models import Group
from rest_framework import permissions


class GroupViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

    def get_queryset(self):
        user = self.request.user
        return (Group.objects.filter(admins=user) | Group.objects.filter(subscribers=user)).distinct()

    permission_classes = [permissions.IsAuthenticated]
