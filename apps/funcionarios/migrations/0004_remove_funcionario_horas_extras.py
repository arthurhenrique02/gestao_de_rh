# Generated by Django 4.1.1 on 2023-03-24 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("funcionarios", "0003_alter_funcionario_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="funcionario",
            name="horas_extras",
        ),
    ]