from django.core.mail import EmailMultiAlternatives, get_connection
from django.utils.http import urlsafe_base64_encode
from django.template.loader import get_template
from django.utils.encoding import force_bytes
# from django.core.mail import get_connection
from django.contrib.auth.models import User
from .tokens import token_generator
from django.conf import settings
from django.contrib import admin

import copy

# validate_users.short_description = "Send validations emails to users" # Prior to Django 3.2
@admin.action(description="Send validations emails to users")
def validate_users(modelAdmin, request, queryset):
  if (modelAdmin.__class__.__name__ == "UserAdmin"):
    users = queryset.filter(is_active=False)
  else:
    user_ids = queryset.filter(user__is_active=False).values_list("user", flat=True)
    users = User.objects.filter(id__in=user_ids)
  
  messages = map(get_validation_message, users)
  send_mass_html_mail(messages)

  modelAdmin.message_user(request,"%d emails sent" % len(users))


def get_validation_message(user):
  subject = "[Example Enterprise] Active su cuenta"
  text_message = "Su cuenta ha sido configurada. Debe acceder al siguiente link para activar su cuenta: %s" % "https://examplenterprise.com"
  from_email = "no-reply@examplenterprise.com"
  recipient = [user.email]
  print(urlsafe_base64_encode(force_bytes(user.id)))
  uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
  token = token_generator.make_token(user)
  html_message = get_template("user_core/validationEmail.html").render({ "uidb64":uidb64, "token":token, "base_url": settings.BASE_URL_BACKEND})
  return (subject,text_message,html_message, from_email, recipient)


def send_mass_html_mail(datatuple, fail_silently=False, auth_user=None,auth_password=None):
    """
    Given a datatuple of (subject, message, html_message, from_email,
    recipient_list), send each message to each recipient list.
    Return the number of emails sent.
    If from_email is None, use the DEFAULT_FROM_EMAIL setting.
    If auth_user and auth_password are set, use them to log in.
    If auth_user is None, use the EMAIL_HOST_USER setting.
    If auth_password is None, use the EMAIL_HOST_PASSWORD setting.
    """
    connection = get_connection(
        # username=auth_user,
        # password=auth_password,
        fail_silently=fail_silently,
    )
    messages = [
        EmailMultiAlternatives(subject, text_message, from_email, recipient,
                               alternatives=[(html_message, 'text/html')],
                               connection=connection)
        for subject, text_message, html_message, from_email, recipient in datatuple
    ]
    return connection.send_messages(messages)