from django.shortcuts import render
from .models import Empresa
from django.views.generic.edit import CreateView


# criar view para o create
class CriarEmpresa(CreateView):
    # criar view a partir do model empresa
    model = Empresa
    fields = ["nome"]
