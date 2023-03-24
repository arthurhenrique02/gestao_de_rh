# Generated by Django 4.1.1 on 2023-03-24 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Documento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nome",
                    models.CharField(help_text="Nome do documento", max_length=100),
                ),
                (
                    "tipo",
                    models.CharField(help_text="Tipo do documento", max_length=100),
                ),
                (
                    "data_postagem",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Data e hora da postagem do documento",
                    ),
                ),
                ("data", models.DateField(help_text="Data de criação do documento")),
            ],
        ),
    ]