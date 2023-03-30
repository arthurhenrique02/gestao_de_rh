from django.db import models
from django.urls import reverse


# definir model da empresa
class Empresa(models.Model):
    # caracteres maximos 100, texto para documentacao e/ou mostrar na tela
    nome = models.CharField(max_length=100, help_text="Nome da empresa")

    # retornar nome da empresa
    def __str__(self):
        return self.nome

    # definir get_absolute_url, metodo para 'reverter' para uma url após updates
    def get_absolute_url(self):
        # irá retornar para a home
        return reverse("home")
