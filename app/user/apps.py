from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'app.user'

    def ready(self):
        # signals are imported, so that they are defined and can be used
        import signals.handler
