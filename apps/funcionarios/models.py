from django.db import models
from django.contrib.auth.models import User

from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


# criar model do funcionário
class Funcionario(models.Model):
    # nome
    nome = models.CharField(max_length=30, help_text="Nome do funcionario")

    # sobrenome
    sobrenome = models.CharField(
        max_length=200, help_text="Sobrenomes do funcionario")

    # user
    # referenciar por username.
    # Deletar utilizando o metodo cascade (o metodo irá deletar o objeto também)
    # Refenciando por OneToOneField, um funcionario so terá acesso a um user, não é necessário o uso de unique=True
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        unique=True
    )

    # idade
    idade = models.IntegerField(
        help_text="Idade do funcionário (apenas numeros)"
    )

    # sexo
    sexo = models.CharField(max_length=1, help_text="Sexo: M ou F")

    # empresa
    # refenciar chave da Empresa ao funcionario, permite apenas uma empresa por funcionario
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    # departamento
    # criar relacionamento (manytomany) para departamentos
    # um funcionario poderá estar presente em mais de um departamento
    departamentos_pertencentes = models.ManyToManyField(Departamento)

    # retornar o nome e sobrenome do funcionario
    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
