from django.db import models


# criar model de horaextra
class ContabilizarHoraExtra(models.Model):
    # quantidade de hora
    quantidade_horas = models.DecimalField(
        max_digits=5, decimal_places=2, help_text="Quantidade de horas extras")

    # motivo das horas
    motivo = models.CharField(
        max_length=250, help_text="Motivo das horas extras")

    # retornar motivo
    def __str__(self):
        return self.motivo
