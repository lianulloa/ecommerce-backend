from rest_framework import generics
from enterprise.decorators.views import withMetadata

class ListAPIViewWithMetadata(generics.ListAPIView):
  @withMetadata
  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

