# Generated by Django 4.1.1 on 2023-03-24 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("empresas", "0001_initial"),
        ("departamentos", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("funcionarios", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="funcionario",
            name="departamento",
        ),
        migrations.AddField(
            model_name="funcionario",
            name="departamentos_pertencentes",
            field=models.ManyToManyField(to="departamentos.departamento"),
        ),
        migrations.AddField(
            model_name="funcionario",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="funcionario",
            name="empresa",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="empresas.empresa"
            ),
        ),
    ]
