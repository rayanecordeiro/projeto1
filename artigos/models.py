from django.db import models
#from equipe.models import Equipe 
from django.core.validators import FileExtensionValidator, MinLengthValidator, MaxLengthValidator
from django.utils import timezone
import os


# Create your models here.
    #um discente pode ter mais de um artigo - caso delete um deleta as duas relacoes 
    #discente = models.ForeignKey(Equipe, on_delete=models.CASCADE)

class Artigos(models.Model):
    FORMATO_ARQUIVO_CHOICES = [
        ('pdf', 'PDF'),
        ('doc', 'DOC'),
        ('docx', 'DOCX'),
    ]

    # Campos obrigatórios
    titulo = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(5, "O título deve ter no mínimo 5 caracteres.")],
        verbose_name="Título",
        null="True"
    )
    autores = models.CharField(
        max_length=255,
        verbose_name="Autores",
        help_text="Separe os autores por vírgula",
        null="True"
    )
    resumo = models.TextField(
        validators=[MinLengthValidator(5, "O resumo deve ter no mínimo 50 caracteres.")],
        verbose_name="Resumo",
        null="True"
    )
    abstract = models.TextField(
        validators=[MinLengthValidator(5, "O abstract deve ter no mínimo 50 caracteres.")],
        verbose_name="Abstract",
        null="True"
    )
    palavras_chave = models.CharField(
        max_length=255,
        verbose_name="Palavras-chave",
        help_text="Separe as palavras-chave por vírgula",
        null="True"
    )
    ano = models.PositiveIntegerField(
        verbose_name="Ano",
        default=timezone.now().year
    )
    revista = models.CharField(
        max_length=255,
        verbose_name="Revista",
        null="True"
    )

    # Campo para upload do arquivo
    arquivo = models.FileField(
        upload_to='artigos/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['pdf', 'doc', 'docx'],
                message="Somente arquivos nos formatos PDF, DOC ou DOCX são permitidos."
            )
        ],
        verbose_name="Arquivo",
        #default='artigos/default.pdf'
        null="True"
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Artigo"
        verbose_name_plural = "Artigos"
        ordering = ['-ano']

    # Validação customizada para garantir ano não superior ao atual
    def clean(self):
        if self.ano > timezone.now().year:
            raise ValidationError({'ano': "O ano não pode ser maior que o ano atual."})