from django.db import models


class Departamento(models.Model):
    # nome
    nome = models.CharField(max_length=200, help_text="Nome do departamento")

    # retornar nome

    def __str__(self):
        return self.nome
