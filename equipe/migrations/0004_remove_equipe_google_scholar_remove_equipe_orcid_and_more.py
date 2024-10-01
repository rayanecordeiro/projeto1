# Generated by Django 5.1.1 on 2024-09-09 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipe', '0003_equipe_github_equipe_google_scholar_equipe_lattes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipe',
            name='google_scholar',
        ),
        migrations.RemoveField(
            model_name='equipe',
            name='orcid',
        ),
        migrations.RemoveField(
            model_name='equipe',
            name='research_gate',
        ),
        migrations.AddField(
            model_name='equipe',
            name='nivel_acesso',
            field=models.CharField(choices=[('Adm', 'Administrador'), ('Basic', 'Basico')], default='Basic', max_length=30),
        ),
    ]
