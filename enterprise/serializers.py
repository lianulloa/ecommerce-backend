from django.db.models import fields
from rest_framework import serializers

import enterprise
from .models import *
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

class ProductSerializer(serializers.ModelSerializer):
  price = serializers.DecimalField(max_digits=9,decimal_places=2,min_value=0.01)

  def validate_enterprise(self, enterprise):
    enterprise = Enterprise.objects.get(id=enterprise.id)
    if enterprise.owner.pk != self.context['request'].user.pk:
      raise serializers.ValidationError("Only the owner of an enterprise can add a product to it")
    return enterprise
  class Meta:
    model = Product
    fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
  user = CustomUserSerializer(read_only=True)
  product = ProductSerializer(read_only=True)
  class Meta:
    model = Rating
    fields = '__all__'