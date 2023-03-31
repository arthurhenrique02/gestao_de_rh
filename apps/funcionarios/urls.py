from django.urls import path, include
from .views import home, ListaFuncionarios


# incluir view home a url dos funcionarios
urlpatterns = [
    # passar como view e setar na root
    path("", ListaFuncionarios.as_view(), name='list_funcionarios'),
]
