from django.db import models

# definir model da empresa


class Empresa(models.Model):
    # caracteres maximos 100, texto para documentacao e/ou mostrar na tela
    nome = models.CharField(max_length=100, help_text="Nome da empresa")
