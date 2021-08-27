from django.shortcuts import render
import logging

from rest_framework import viewsets, permissions, mixins, generics

from .serializers import EnterpriseSerializer, CategorySerializer, SubCategorySerializer
from .models import *

logger = logging.getLogger("mfc")
class EnterpriseViewSet(viewsets.ModelViewSet):
  queryset = Enterprise.objects.all()
  serializer_class = EnterpriseSerializer

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user.customuser)

class CategoryListView(mixins.ListModelMixin, generics.GenericAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

  def get(self, request, *args, **kwargs):
    if self.request.query_params.get("metadata"):
      response = self.list(request, *args, * kwargs)
      response.data = {
        'data': response.data,
        'metadata': {
          'total': self.get_queryset().count()
        }
      }
      return response
    return self.list(request, *args, **kwargs)

class SubcategoryListView(mixins.ListModelMixin, generics.GenericAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

  def get_queryset(self):
    return Category.objects.get(id=self.kwargs['pk']).subcategory_set

  def get(self, request, *args, **kwargs):
    if self.request.query_params.get("metadata"):
      response = self.list(request, *args, * kwargs)
      response.data = {
        'data': response.data,
        'metadata': {
          'total': self.get_queryset().count()
        }
      }
      return response
    return self.list(request, *args, **kwargs)