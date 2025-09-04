from django.shortcuts import render, redirect
from .forms import PunicoesForm
from .models import Punições

def criar_punicao(request):
    if request.method == 'POST':
        form = PunicoesForm(request.POST)
        if form.is_valid():
            punicao_salva = form.save()
            

            mensagem = (
                f'Nome: {punicao_salva.nick_name.nome}\n'
                f'ID: {punicao_salva.id_punido}\n'
                f'Motivo: {punicao_salva.motivo.nome}\n'
                f'Tempo: {punicao_salva.temp_ban} dias\n'
                f'Provas: {punicao_salva.link_evid}\n'
            )
            
            return render(request, 'denuncias/punicao_sucesso.html', {'mensagem': mensagem})
    else:
        form = PunicoesForm()

    return render(request, 'denuncias/criar_punicao.html', {'form': form})