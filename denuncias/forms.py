from django import forms
from .models import Punições, Motivo, Vares, Acoes

class PunicoesForm(forms.ModelForm):
    class Meta:
        model = Punições
        fields = ['nick_name', 'id_punido', 'id_dc', 'motivo', 'temp_ban', 'link_evid','codigo_tx']

    def clean_temp_ban(self):
        data = self.cleaned_data["temp_ban"]
        try:
            int(data)
        except ValueError:
            if data not in ['INDETERMINADO','Indeterminado','indeterminado']:
                raise forms.ValidationError("O campo aceita apenas números ou a palavra 'Indeterminado'.") ##arruma e subir pro main essa mensagem
        return data

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
