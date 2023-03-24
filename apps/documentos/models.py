from django.db import models


# criar classe documento
class Documento(models.Model):
    # nome
    nome = models.CharField(max_length=100, help_text="Nome do documento")
    # tipo do documento
    tipo = models.CharField(max_length=100, help_text="Tipo do documento")
    # data que foi inserido no sistema
    data_postagem = models.DateTimeField(
        auto_now_add=True, help_text="Data e hora da postagem do documento")
    # data do documento
    data = models.DateField(help_text="Data de criação do documento")
