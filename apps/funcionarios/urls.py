from django.urls import path, include
from .views import ListaFuncionarios, AtualizarFuncionario


# incluir view home a url dos funcionarios
urlpatterns = [
    # passar como view e setar na root
    path("", ListaFuncionarios.as_view(), name="list_funcionarios"),
    path(
        "atualizar_funcionario/<int:pk>",
        AtualizarFuncionario.as_view(),
        name="atualizarFuncionario"
    ),

]
