from django import forms
from .models import Artigos

#editar os campos de busca de forma inline aqui
class ArtigosSearchForm(forms.Form):
    search = forms.CharField(required=False, label="Título")
    autor = forms.CharField(required=False, label="Autor")
    revista = forms.CharField(required=False, label="Revista")
    palavras_chave = forms.CharField(required=False, label="Palavras-chave")
    ano = forms.IntegerField(required=False, label="Ano")
    resumo = forms.CharField(required=False, label="Resumo")

class ArtigosForm(forms.ModelForm):
    class Meta:
        model = Artigos
        fields = ['titulo', 'autores', 'revista', 'palavras_chave', 'ano', 'resumo', 'abstract','arquivo']  # Campos que deseja incluir no formulário
