from django.db.models import fields
from django_filters import rest_framework as filters
from enterprise.models import *

class ProductFilter(filters.FilterSet):
  price = filters.RangeFilter() # enables price_min and price_max as filters
  class Meta:
    model = Product
    fields = ['name', 'description', 'subcategory', 'enterprise', 'price']
    filter_overrides = {
      models.CharField: {
          'filter_class': filters.CharFilter,
          'extra': lambda f: {
              'lookup_expr': 'icontains',
          },
      },
      models.TextField: {
          'filter_class': filters.CharFilter,
          'extra': lambda f: {
              'lookup_expr': 'icontains',
          },
      }
    }
