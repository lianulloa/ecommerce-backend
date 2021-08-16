from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

#Inside PasswordResetTokenGenerator implementation a setting can be found to set a limit for the time
#a token remains valid
class ActivateUserTokenGenerator(PasswordResetTokenGenerator):
  def _make_hash_value(self, user, timestamp):
    return (
      six.text_type(user.pk) + six.text_type(timestamp) +
      #this next line is what makes a token invalid after user has been activated
      six.text_type(user.is_active)
    )
token_generator = ActivateUserTokenGenerator()