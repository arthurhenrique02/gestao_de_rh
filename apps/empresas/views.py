from django.shortcuts import render
from .models import Empresa
from django.views.generic.edit import CreateView


# criar view para o create
class CriarEmpresa(CreateView):
    # criar view a partir do model empresa
    model = Empresa
    fields = ["nome"]

    # definir metodo form valid
    # o metodo toma como parametros a propria classe e o form utilizado
    def form_valid(self, form):
        # criar objeto para salvar form
        # será retornado um objeto, nesse caso, o objeto Empresa
        Empresa_objeto = form.save()

        # pegar objeto funcionario da request,
        funcionario = self.request.user.funcionario

        # adicionar Empresa ao funcionario
        funcionario.empresa = Empresa_objeto

        # salvar no Bd a alteração
        funcionario.save()
