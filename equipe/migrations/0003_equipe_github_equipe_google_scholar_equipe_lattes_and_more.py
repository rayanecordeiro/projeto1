# Generated by Django 5.1.1 on 2024-09-09 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipe', '0002_equipe_registro_atualizado_equipe_registro_criado'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='equipe',
            name='google_scholar',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='equipe',
            name='lattes',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='equipe',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='equipe',
            name='orcid',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='equipe',
            name='research_gate',
            field=models.URLField(blank=True, null=True),
        ),
    ]