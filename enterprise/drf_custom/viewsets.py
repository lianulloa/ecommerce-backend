from rest_framework import viewsets, mixins
from enterprise.decorators.views import withMetadata

class ModelViewSetWithMetadata(viewsets.ModelViewSet):
  @withMetadata
  def list(self, request, *args, **kwargs):
    return mixins.ListModelMixin.list(self, request, *args, **kwargs)
