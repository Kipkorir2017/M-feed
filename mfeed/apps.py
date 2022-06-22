from django.apps import AppConfig


class MfeedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mfeed'

    def ready(self) -> None:
        import mfeed.signals