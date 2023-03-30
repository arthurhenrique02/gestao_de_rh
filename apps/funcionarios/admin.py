from django.contrib import admin

from .models import Funcionario


# criar model para Funcionario em admin
class FuncionarioAdmin(admin.ModelAdmin):
    # mostra lista de elementos
    # impossibilitado de mostrar departamentos, pois é uma conexao ManyToMany
    list_display = ["nome", "sobrenome", "user", "idade", "empresa"]


# registrar funcionario
admin.site.register(Funcionario, FuncionarioAdmin)
