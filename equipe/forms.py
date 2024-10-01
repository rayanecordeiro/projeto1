from django.forms import ModelForm
from .models import Equipe

class EquipeForm(ModelForm):
    class Meta:
        model = Equipe
        # Exclui o campo 'nivel_acesso' do formulário
        exclude = ['nivel_acesso']
