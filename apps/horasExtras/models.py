from django.db import models

from apps.funcionarios.models import Funcionario


# criar model de horaextra
class ContabilizarHorasExtra(models.Model):
    # quantidade de hora
    quantidade_horas = models.DecimalField(
        max_digits=5, decimal_places=2, help_text="Quantidade de horas extras")

    # motivo das horas
    motivo = models.CharField(
        max_length=250, help_text="Motivo das horas extras")

    # hora extra pertencente ao funcionário
    # referenciar Funcionario
    # ao deletar (on_delete) proteger o objeto (não excluí-lo de primeira)
    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.PROTECT,
    )

    # retornar motivo
    def __str__(self):
        return self.motivo
