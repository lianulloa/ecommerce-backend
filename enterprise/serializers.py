from django.db.models import fields
from rest_framework import serializers
from .models import Category, Enterprise, CustomUser, SubCategory
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

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = SubCategory
    fields = '__all__'
