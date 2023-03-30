from django.contrib import admin

from .models import Empresa


# criar model para Empresa em admin
class EmpresaAdmin(admin.ModelAdmin):
    # mostra lista de elementos
    list_display = ["nome",]


# adcionar model ao admin site
admin.site.register(Empresa, EmpresaAdmin)
