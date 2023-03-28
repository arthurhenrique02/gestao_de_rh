from django.urls import path, include
from .views import CriarEmpresa


# incluir view criarEmpresa a url
# criar rotar "registrarEmpresa" e adicionar a view
urlpatterns = [
    # adicionar a view CriarEmpresa como uma view (.as_view()) e setar o nome da rota como registrar_empresa
    path("registrarEmpresa", CriarEmpresa.as_view(), name="Registrar_empresa"),
]
