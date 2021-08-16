from django.shortcuts import render
import logging

from rest_framework import viewsets, permissions

from .serializers import EnterpriseSerializer
from .models import *

logger = logging.getLogger("mfc")
class EnterpriseViewSet(viewsets.ModelViewSet):
  queryset = Enterprise.objects.all()
  serializer_class = EnterpriseSerializer

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user.customuser)
