from django.shortcuts import render
import logging

from rest_framework import filters
from rest_framework.exceptions import ValidationError

from .serializers import *
from .decorators.views import withMetadata
from .drf_custom.generics import ListAPIViewWithMetadata
from .drf_custom.viewsets import ModelViewSetWithMetadata
# from .models import *

logger = logging.getLogger("mfc")
class EnterpriseViewSet(ModelViewSetWithMetadata):
  queryset = Enterprise.objects.all()
  serializer_class = EnterpriseSerializer

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user.customuser)

class ProductViewSet(ModelViewSetWithMetadata):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  filter_backends = [filters.SearchFilter]
  search_fields = ['name', 'description']

  def perform_destroy(self, instance):
    if self.request.user.pk != instance.enterprise.owner.pk:
      raise ValidationError('Only the owner of an enterprise can delete a product of it')
    instance.delete()

class RatingViewSet(ModelViewSetWithMetadata):
  queryset = Rating.objects.all()
  serializer_class = RatingSerializer

  def perform_create(self, serializer):
    serializer.save(user=self.request.user.customuser)

class CategoryListView(ListAPIViewWithMetadata):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class SubcategoryListView(ListAPIViewWithMetadata):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

  def get_queryset(self):
    return Category.objects.get(id=self.kwargs['pk']).subcategory_set
