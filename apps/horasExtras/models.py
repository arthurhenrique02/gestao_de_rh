from django.db import models


# criar model de horaextra
class ContabilizarHoraExtra(models.Model):
    # quantidade de hora
    quantidade_horas = models.DecimalField(
        max_digits=5, decimal_places=2, help_text="Quantidade de horas extras")
