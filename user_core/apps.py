from django.apps import AppConfig


class UserCoreConfig(AppConfig):
    name = 'user_core'

    def ready(self):
        from . import signals