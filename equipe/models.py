from django.db import models

# Create your models here.
class Equipe(models.Model):
    #nome do integrante
    nome = models.CharField(max_length=200)

    #formacao academica do integrante
    fa = (
        ("G", "Graduacao"),
        ("M", "Mestrado"),
        ("D", "Doutorado"),
    )
    formacao_academica = models.CharField(max_length=30, choices=fa, default="G")

    #nivel de acesso do integrante
    na = (
        ("Adm", "Administrador"),
        ("Basic", "Basico"),
    )
    nivel_acesso = models.CharField(max_length=30, choices=na, default="Basic")


    #email do integrante
    email = models.EmailField(max_length=100, null=True, blank=True)

    #data e hora que o registro foi criado
    registro_criado = models.DateTimeField(auto_now_add=True)

    #data e hora que o registro foi atualizado
    registro_atualizado = models.DateTimeField(auto_now=True)

    #modelos de urls aceitas
    lattes = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome