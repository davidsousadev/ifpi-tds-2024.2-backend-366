# Generated by Django 5.1.4 on 2025-01-22 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ativa', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='projeto',
            name='orcamento',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Orçamento'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='equipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projetos', to='nucleo.equipe'),
        ),
    ]
