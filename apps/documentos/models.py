from django.db import models

from apps.funcionarios.models import Funcionario


# criar classe documento
class Documento(models.Model):
    # nome
    nome = models.CharField(max_length=100, help_text="Nome do documento")

    # tipo do documento
    tipo = models.CharField(max_length=100, help_text="Tipo do documento")

    # data que foi inserido no sistema
    data_postagem = models.DateTimeField(
        auto_now_add=True,  # auto adicionar a data de postagem
        help_text="Data e hora da postagem do documento")

    # data do documento
    data = models.DateField(help_text="Data de criação do documento")

    # conectar o documento com o funcionario pertencente atraves do username
    # ao deletar (on_delete) proteger o documento/objeto (não exluí-lo de primeira)
    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.PROTECT,
    )

    # retornar nome
    def __str__(self):
        return self.nome
