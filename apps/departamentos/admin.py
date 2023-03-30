from django.contrib import admin

from .models import Departamento


# criar model para departamentos no admin
class DepartamentoAdmin(admin.ModelAdmin):
    # mostra a lista de elementos
    list_display = ["nome",]


# adcionar model
admin.site.register(Departamento, DepartamentoAdmin)
