from django.apps import AppConfig
from django.db.models.signals import post_save

class AccountConfig(AppConfig):
    name = 'account'
    def ready(self):
        from django.contrib.auth import get_user_model
        from .signals import create_profile
        post_save.connect(create_profile,sender=get_user_model())
        