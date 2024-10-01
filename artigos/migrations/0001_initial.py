# Generated by Django 5.1.1 on 2024-09-09 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipe', '0003_equipe_github_equipe_google_scholar_equipe_lattes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artigos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('discente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipe.equipe')),
            ],
        ),
    ]