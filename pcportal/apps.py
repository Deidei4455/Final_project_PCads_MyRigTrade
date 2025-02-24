from django.apps import AppConfig


class PcportalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pcportal'

    def ready(self):
        from .signals import create_profile_and_seller
