def withMetadata(method):
  def inner(view, request, *args, **kwargs):
    if request.query_params.get("metadata"):
      response = method(view, request, *args, * kwargs)
      response.data = {
        'data': response.data,
        'metadata': {
          'total': view.get_queryset().count()
        }
      }
      return response
    return method(view, request, *args, **kwargs)
  return inner