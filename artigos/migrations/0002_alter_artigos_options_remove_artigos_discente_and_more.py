# Generated by Django 5.1.1 on 2024-09-09 08:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artigos',
            options={'ordering': ['-ano'], 'verbose_name': 'Artigo', 'verbose_name_plural': 'Artigos'},
        ),
        migrations.RemoveField(
            model_name='artigos',
            name='discente',
        ),
        migrations.AddField(
            model_name='artigos',
            name='abstract',
            field=models.TextField(null='True', validators=[django.core.validators.MinLengthValidator(5, 'O abstract deve ter no mínimo 50 caracteres.')], verbose_name='Abstract'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='artigos',
            name='ano',
            field=models.PositiveIntegerField(default=2024, validators=[django.core.validators.MinLengthValidator(4, 'Ano inválido.'), django.core.validators.MaxLengthValidator(4, 'Ano inválido.')], verbose_name='Ano'),
        ),
        migrations.AddField(
            model_name='artigos',
            name='arquivo',
            field=models.FileField(null='True', upload_to='artigos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'], message='Somente arquivos nos formatos PDF, DOC ou DOCX são permitidos.')], verbose_name='Arquivo'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='artigos',
            name='autores',
            field=models.CharField(help_text='Separe os autores por vírgula', max_length=255, null='True', verbose_name='Autores'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='artigos',
            name='palavras_chave',
            field=models.CharField(help_text='Separe as palavras-chave por vírgula', max_length=255, null='True', verbose_name='Palavras-chave'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='artigos',
            name='resumo',
            field=models.TextField(null='True', validators=[django.core.validators.MinLengthValidator(5, 'O resumo deve ter no mínimo 50 caracteres.')], verbose_name='Resumo'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='artigos',
            name='revista',
            field=models.CharField(max_length=255, null='True', verbose_name='Revista'),
            preserve_default='True',
        ),
        migrations.AlterField(
            model_name='artigos',
            name='titulo',
            field=models.CharField(max_length=255, null='True', validators=[django.core.validators.MinLengthValidator(5, 'O título deve ter no mínimo 5 caracteres.')], verbose_name='Título'),
        ),
    ]
