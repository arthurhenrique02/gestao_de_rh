from django.urls import path, include
from .views import CriarEmpresa, EditarEmpresa


# incluir view criarEmpresa a url
# criar rotar "registrarEmpresa" e adicionar a view
urlpatterns = [
    # adicionar a view CriarEmpresa como uma view (.as_view()) e setar o nome da rota como registrar_empresa
    path(
        "registrarEmpresa",
        CriarEmpresa.as_view(),
        name="Registrar_empresa"
    ),

    # definir rota de update da empresa, criá-la como uma view
    # necessario passar o id da empresa dentro da url <int:pk>
    path(
        "editarEmpresa/<int:pk>",
        EditarEmpresa.as_view(),
        name="Editar_empresa"
    ),
]
