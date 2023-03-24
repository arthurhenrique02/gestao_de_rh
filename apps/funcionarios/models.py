from django.db import models


# criar model do funcionário
class Funcionario(models.Model):
    # nome
    nome = models.CharField(max_length=30, help_text="Nome do funcionario")
    # sobrenome
    sobrenome = models.CharField(
        max_length=200, help_text="Sobrenomes do funcionario")
    # idade
    idade = models.IntegerField(
        help_text="Idade do funcionário (apenas numeros)")
    # sexo
    sexo = models.CharField(max_length=1, help_text="Sexo: M ou F")
    # empresa
    empresa = models.CharField(
        max_length=100, help_text="Empresa que o funcionario trabalha")

    # departamento
    departamento = models.CharField(
        max_length=100, help_text="Departamento que está alocado")

    # Quantidade de horas extras
    horas_extras = models.DecimalField(
        max_digits=5, decimal_places=2, help_text="Quantidade de horas extras")

    # retornar o nome e sobrenome do funcionario
    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
