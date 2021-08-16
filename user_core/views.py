# APP IMPORTS
from .serializers import CustomUserSerializer, UserSerializer
from .authentication import Uidb64Authentication
from .models import *

# DJANGO IMPORTS
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.conf import settings

# REST_FRAMEWORK IMPORTS
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import mixins, generics, viewsets, status
# from rest_framework import status

import logging
mfc_logger = logging.getLogger("mfc")

# It is highly possible that this will be changed into Viewset in the future
class UserView(mixins.CreateModelMixin, generics.GenericAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = UserSerializer

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

class CustomUserViewSet(viewsets.ModelViewSet):
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserSerializer

  def retrieve(self, request, pk=None):
    user = None
    try:
      if request.user.is_authenticated: #session cookie is set
        user = request.user
        user = user.customuser
      else:
        user = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
      if not user: # session cookie is not set
        user = get_object_or_404(User, pk=pk)
      data = UserSerializer(instance=user).data
      response_data = {}
      for key,value in data.items():
        response_data[key]= value
      return Response({ "user": response_data }, status=status.HTTP_200_OK)

    serializer = CustomUserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([Uidb64Authentication])
def activate(request, **kwargs):
  user = request.user
  user.is_active = True
  user.save()
  login(request, user)
  return redirect(settings.BASE_URL + "/account-activated/"+ str(user.id))