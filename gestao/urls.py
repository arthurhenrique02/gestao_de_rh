from django.contrib import admin
from django.urls import path, include


# url paths
urlpatterns = [
    # adicionar rota padrao padrao ("") para o app, definido para o app principal, que irá mostrar uma interface de inicio
    path("", include("apps.coreApp.urls")),
    # adicionar urls dos funcionarios a rota
    path("funcionarios/", include("apps.funcionarios.urls")),
    # adicionar rotas de empresas
    path("empresa/", include("apps.empresas.urls")),
    # adicionar rota de departamentos
    path("departamentos/", include("apps.departamentos.urls")),
    # adicionar path para o login, o path é do proprio django e irá conter algumas outras funcionalidades como login e logout
    path('accounts/', include('django.contrib.auth.urls')),

    path("admin/", admin.site.urls),
]
