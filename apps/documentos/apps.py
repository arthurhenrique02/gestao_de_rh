from django.apps import AppConfig


class DocumentosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    # necessario adcionar o path "apps.", de acordo com a doc do django
    name = "apps.documentos"
