from rest_framework import viewsets
from enterprise.decorators.views import withMetadata

class ModelViewSetWithMetadata(viewsets.ModelViewSet):
  @withMetadata
  def list(self, request, *args, **kwargs):
    return super().list(self, request, *args, **kwargs)
