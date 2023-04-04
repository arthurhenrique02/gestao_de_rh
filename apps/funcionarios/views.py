from random import randint
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.models import User

from .models import Funcionario


# view para cadastrar um novo funcionario
class RegistrarFuncionario(CreateView):
    # definir model
    model = Funcionario

    # campos
    fields = ["nome", "sobrenome", "idade",
              "sexo", "departamentos_pertencentes"]

    # definir metodo form valid
    def form_valid(self, form):
        # pegar o objeto funcionario que está sendo criado
        # commit false garante que não vá direto para o banco de dados
        funcionario = form.save(commit=False)

        # definir a empresa
        funcionario.empresa = self.request.user.funcionario.empresa

        # definir username
        # pegar o nome e o primeiro sobrenome e um numero aleatorio
        username = (
            funcionario.nome +
            funcionario.sobrenome.split(" ")[0] +
            str(randint(0, 1000))
        )
        funcionario.user = User.objects.create(username=username)

        # salvar no banco de dados
        funcionario.save()

        # retornar um supe para chamar o form valid
        return super(RegistrarFuncionario, self).form_valid(form)


# definir classe para listar (read) funcionarios
class ListaFuncionarios(ListView):
    # definir model
    model = Funcionario

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
