from django.db.models import fields
from rest_framework import serializers
from .models import Enterprise, CustomUser
from user_core.serializers import CustomUserSerializer
import logging
logger = logging.getLogger("mfc")

class EnterpriseSerializer(serializers.ModelSerializer):
  owner = CustomUserSerializer(read_only=True)

  # def create(self, validated_data):
  #   owner = CustomUser.objects.first()
  #   return Enterprise.objects.create(**validated_data, owner= owner)

  class Meta:
    model = Enterprise
    exclude = ["followers","likes"]