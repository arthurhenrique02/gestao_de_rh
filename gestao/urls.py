"""gestao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path 
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views


# url paths
urlpatterns = [
    # adicionar rota padrao padrao ("") para o app, definido para o app principal, que irá mostrar uma interface de inicio
    path("", include("apps.coreApp.urls")),
    # adicionar urls dos funcionarios a rota
    path("funcionarios/", include("apps.funcionarios.urls")),

    path("admin/", admin.site.urls),
    # adicionar path para o login, o path é do proprio django e irá conter algumas outras funcionalidades como login e logout
    path('accounts/', include('django.contrib.auth.urls')),

]
