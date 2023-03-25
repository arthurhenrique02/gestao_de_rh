from django.urls import path, include
from .views import home


# incluir view home a url do app principal
# criado rota para linkar com a rota padrao("") do app gestao
urlpatterns = [
    # setar como root
    path("", home),
]
