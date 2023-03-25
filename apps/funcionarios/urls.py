from django.urls import path, include
from .views import home


# incluir view home a url dos funcionarios
urlpatterns = [
    # setar como root
    path("", home),
]
