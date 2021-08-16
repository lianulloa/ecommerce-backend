from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import *

class UserSerializer(serializers.ModelSerializer):
  # password = serializers.CharField(write_only=True)
  def create(self, validated_data):
      user = User.objects.create(**validated_data)
      user.set_password(validated_data['password'])
      user.is_active = False
      user.save()
      return user

  class Meta:
    model = User
    fields = '__all__'
    extra_kwargs = {
      'username': {
        'validators': [
          UniqueValidator(
            queryset=User.objects.all(),
            message='Ya existe un usuario con este correo electrónico'
          )
        ]
      },
      'password': {
        'write_only': True
      },
    }

class CustomUserSerializer(serializers.ModelSerializer):
  user = UserSerializer()

  def create(self, validated_data):
    """
    Create and return a new `CustomUser` instance, given the validated data.
    """
    user_data = validated_data.pop('user')
    user_serializer = UserSerializer(data=user_data)
    if user_serializer.is_valid():
      user = user_serializer.save()
    return CustomUser.objects.create(user=user, **validated_data)

  class Meta:
    model = CustomUser
    fields = ['user', 'phone_number', 'city', 'country']