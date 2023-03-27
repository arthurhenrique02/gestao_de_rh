# Generated by Django 4.1.1 on 2023-03-24 22:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("funcionarios", "0002_remove_funcionario_departamento_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="funcionario",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]