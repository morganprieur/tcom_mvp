from django.apps import AppConfig


class uthdemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'uthdemo'

    def ready(self):
        # pass 
        # Implicitly connect signal handlers decorated with @receiver. 
        from . import signals 
