from django.apps import AppConfig


class AdvertisingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.advertising'

    def ready(self):
        import apps.advertising.signals