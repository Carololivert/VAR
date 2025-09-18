from django import forms
from .models import Punições, Motivo, Vares

class PunicoesForm(forms.ModelForm):
    class Meta:
        model = Punições
        fields = ['nick_name', 'id_punido', 'id_dc', 'motivo', 'temp_ban', 'link_evid']


class VarForm(forms.ModelForm):
    class Meta:
        model = Vares
        fields = ['nome']