from django.db import models
from django.conf import settings

# Create your models here.
class CustomUser(models.Model):
  """Model definition for CustomUser."""
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
  phone_number = models.CharField(max_length=15, unique=True)
  city = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    """Meta definition for CustomUser."""

    verbose_name = 'Info Adicional de usuario'
    verbose_name_plural = 'Info adicional de los usuarios'

  def __str__(self):
    """Unicode representation of CustomUser."""
    return self.user.username


# class AccountActivationToken(models.Model):
#   	user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True,on_delete=models.CASCADE)
# 	uidb64 = models.CharField(max_length=10)
# 	token = models.CharField(max_length=50)
# 	created_at = models.DateField(auto_now=True)
# 	class Meta:
# 		verbose_name = "Token de Activación de Cuenta"
# 		verbose_name_plural = "Tokens de Activación de Cuenta"

# 	def __str__(self):
# 		return "Activation for %s" % self.user.email
	
# class ChangePasswordToken(models.Model):
# 	user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True,on_delete=models.CASCADE)
# 	uidb64 = models.CharField(max_length=10)
# 	token = models.CharField(max_length=50)
# 	created_at = models.DateField(auto_now_add=True)
# 	class Meta:
# 		verbose_name = "Token de Cambio de Contraseña"
# 		verbose_name_plural = "Tokens de Cambio de Contraseña"

# 	def __str__(self):
# 		return "Change Password's token for %s" % self.user.email
	
