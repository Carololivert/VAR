from django import forms
from .models import Punições, Motivo, Vares, Acoes

class PunicoesForm(forms.ModelForm):
    class Meta:
        model = Punições
        fields = ['nick_name', 'id_punido', 'id_dc', 'motivo', 'temp_ban', 'link_evid']


class VarForm(forms.ModelForm):
    class Meta:
        model = Vares
        fields = ['nome']

class ReuniaoForm(forms.Form):
    escolha_var = forms.ModelChoiceField(
        queryset=Vares.objects.all(),
        label='Var'
    )

class TelaForm(forms.Form):
    escolha_var = forms.ModelChoiceField(
        queryset=Vares.objects.all(),
        label='Var'
    )
    escolha_acao = forms.ModelChoiceField(
        queryset=Acoes.objects.all(),
        label='Selecione a açao'
    )
