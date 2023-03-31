from django.shortcuts import render, redirect
from .models import Empresa
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse


# criar view para o create
class CriarEmpresa(CreateView):
    # criar view a partir do model empresa
    model = Empresa
    # criar fields
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

        # retornar para a url raiz
        return redirect("/", messages=messages)


# Criar view para editar empresa
# herda metodo Update view
class EditarEmpresa(UpdateView):
    # criar view a partir do model empresa
    model = Empresa

    # criar fields
    fields = ["nome"]
