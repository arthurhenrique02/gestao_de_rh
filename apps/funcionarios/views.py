from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from .models import Funcionario


# definir view home
# request como argumento para poder pegar a requisição do usuário
def home(request):
    return HttpResponse("Ola mundo!")


# definir classe para listar funcionarios
class ListaFuncionarios(ListView):
    # definir model
    model = Funcionario

    # definir paginação
    paginate_by = 10

    # alterar queryset para apenas a empresa pertencente ao funcionario logado
    def get_queryset(self):
        # pegar a empresa do funcionario logado
        empresa_logada = self.request.user.funcionario.empresa

        # mudar query
        return Funcionario.objects.filter(empresa=empresa_logada)
