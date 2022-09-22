from django.apps import AppConfig


class NewzConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newz'

    def ready(self):
        from scheduler import updater
        updater.start()