from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text
from django.contrib.auth.models import User

from rest_framework import authentication
from rest_framework import exceptions

from .tokens import token_generator


import logging
log = logging.getLogger("mfc")

class Uidb64Authentication(authentication.BaseAuthentication):
  def authenticate(self, request):
    uidb64, token = request.path.split('/')[-2].split('.')

    if not uidb64:
      return None

    try:
      uid = force_text(urlsafe_base64_decode(uidb64))
      user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
      raise exceptions.AuthenticationFailed('No such user')

    if token_generator.check_token(user, token):
      return (user, None)

    raise exceptions.AuthenticationFailed('No such user')


    # username = request.META.get('HTTP_X_USERNAME')
    # if not username:
    #     return None

    # try:
    #     user = User.objects.get(username=username)
    # except User.DoesNotExist:
    #     raise exceptions.AuthenticationFailed('No such user')
