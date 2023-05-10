from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions

from .serializers import MiniAppsSerializer

from ..models import MiniApps

class MiniAppsViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = MiniAppsSerializer
    queryset = MiniApps.objects.all()

    def get_queryset(self):
        user = self.request.user
        return MiniApps.objects.filter(admins=user)

    permission_classes = [permissions.IsAuthenticated]
