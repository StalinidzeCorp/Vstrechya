from django.apps import AppConfig


class CeleryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "celeryapp"
    verbose_name = "Celeryapp"
