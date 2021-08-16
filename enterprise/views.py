from django.shortcuts import render

from rest_framework import viewsets, permissions

from .serializers import EnterpriseSerializer
from .models import *

class EnterpriseViewSet(viewsets.ModelViewSet):
  queryset = Enterprise.objects.all()
  serializer_class = EnterpriseSerializer
  # FIXME: remove this when authentication gets implemented
  permission_classes = [permissions.AllowAny]

  def perform_create(self, serializer):
    owner = CustomUser.objects.first()
    serializer.save(owner=owner)
    # serializer.save(owner=self.request.user)
