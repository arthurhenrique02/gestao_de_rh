from django.urls import path, include
from .views import ListaFuncionarios, AtualizarFuncionario, DeletarFuncionario, RegistrarFuncionario


# incluir view home a url dos funcionarios
urlpatterns = [
    # passar como view
    # url para cadastrar um novo funcionario
    path(
        "registrar_funcionario/",
        RegistrarFuncionario.as_view(),
        name="registrarFuncionario"
    ),

    # url para listar (read) os funcionarios (está na raiz de funcionarios/)
    path("", ListaFuncionarios.as_view(), name="list_funcionarios"),

    # url de update
    path(
        "atualizar_funcionario/<int:pk>",
        AtualizarFuncionario.as_view(),
        name="atualizarFuncionario"
    ),

    # url para deletar funcionario
    path(
        "deletar_funcionario/<int:pk>",
        DeletarFuncionario.as_view(),
        name="deletarFuncionario"
    ),
]
