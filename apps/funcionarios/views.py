from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
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


# view para atualizar o cadastro do funcionario
class AtualizarFuncionario(UpdateView):
    model = Funcionario

    fields = [
        "nome", "sobrenome", "idade", "sexo",
        "departamentos_pertencentes",
    ]


# view para deletar
class DeletarFuncionario(DeleteView):
    # definir model
    model = Funcionario

    # definir url de retorno (sucesso ao deletar)
    success_url = reverse_lazy("list_funcionarios")
