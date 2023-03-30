from django.contrib import admin

from .models import Documento


# criar model para Documento em admin
class DocumentoAdmin(admin.ModelAdmin):
    # mostra lista
    list_display = ["nome", "tipo", "data_postagem", "data", "funcionario"]


# registrar model
admin.site.register(Documento, DocumentoAdmin)
