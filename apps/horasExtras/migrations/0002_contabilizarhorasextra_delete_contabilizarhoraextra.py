# Generated by Django 4.1.1 on 2023-03-24 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("funcionarios", "0002_remove_funcionario_departamento_and_more"),
        ("horasExtras", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContabilizarHorasExtra",
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
                    "quantidade_horas",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Quantidade de horas extras",
                        max_digits=5,
                    ),
                ),
                (
                    "motivo",
                    models.CharField(
                        help_text="Motivo das horas extras", max_length=250
                    ),
                ),
                (
                    "funcionario",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="funcionarios.funcionario",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="ContabilizarHoraExtra",
        ),
    ]
