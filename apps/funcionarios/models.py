from django.db import models
from django.contrib.auth.models import User

from apps.departamentos.models import Departamento


# criar model do funcionário
class Funcionario(models.Model):
    # nome
    nome = models.CharField(max_length=30, help_text="Nome do funcionario")

    # sobrenome
    sobrenome = models.CharField(
        max_length=200, help_text="Sobrenomes do funcionario")

    # user
    # referenciar por username.
    # Deletar utilizando o metodo cascade
    # (o metodo irá aos outros BDs e irá apagar itens que estao referenciados pelo user digitado)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # idade
    idade = models.IntegerField(
        help_text="Idade do funcionário (apenas numeros)")

    # sexo
    sexo = models.CharField(max_length=1, help_text="Sexo: M ou F")

    # empresa
    empresa = models.CharField(
        max_length=100,
        help_text="Empresa que o funcionario trabalha"
    )

    # departamento
    # criar refenciamento (manytomany) para departamentos
    departamentos_pertencentes = models.ManyToManyField(Departamento)

    # Quantidade de horas extras
    horas_extras = models.DecimalField(
        max_digits=5, decimal_places=2,
        help_text="Quantidade de horas extras"
    )

    # retornar o nome e sobrenome do funcionario

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
