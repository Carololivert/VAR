from django.shortcuts import render, redirect
from .forms import PunicoesForm, TelaForm, VarForm,Vares,ReuniaoForm
from .models import Punições
from datetime import datetime, timedelta
import datetime

def criar_punicao(request):
    if request.method == 'POST':
        form = PunicoesForm(request.POST)
        if form.is_valid():
            punicao_salva = form.save()


            mensagem = (
                f'**ID: {punicao_salva.id_punido}**\n'
                f'ID Discord: {punicao_salva.id_dc}\n'
                f'Motivo: {punicao_salva.motivo.nome}\n'
                f'Tempo: {punicao_salva.temp_ban} dias\n'
                f'Provas: {punicao_salva.link_evid}\n'
            )

            msg = ( 
                f'Sua allowlist está sendo removida por {punicao_salva.temp_ban} dias, por conduta inadequada no Complexo XP.\n'
                f'Segue nossa análise: {punicao_salva.motivo.nome}'
            )
            contexto = {
                'mensagem' : mensagem,
                'msg' : msg 
            }
            return render(request, 'denuncias/punicao_sucesso.html', contexto)
    else:
        form = PunicoesForm()

    return render(request, 'denuncias/criar_punicao.html', {'form': form})

def criar_var(request):
    if request.method == 'POST':
        form = VarForm(request.POST)
        if form.is_valid():
            var_salvo = form.save()

            msg = (
                f'Var {var_salvo.nome} foi salvo no banco de dados.'
            )

        return render(request, 'denuncias/var_sucesso.html', {'mensagem':msg})
    else:
        form = VarForm()
        return render(request, 'denuncias/criar_var.html', {'form': form})
    
def exibir_vares(request):
    pessoas = Vares.objects.all()
    contexto = {'pessoas': pessoas}
    return render(request, 'denuncias/exibir_vares.html', contexto)

def chamar_reuniao(request):
    if request.method == 'POST':
        form = ReuniaoForm(request.POST)
        
        if form.is_valid():
            pessoa = form.cleaned_data['escolha_var']
            mensagem = (
                f'Boa noite, você está sendo convidado(a) a participar de uma reunião com a Administração. Procure o {pessoa.nome}, para agendar um horário, na data de hoje ou amanhã ({data_hoje.strftime('%d/%m/%Y')} ou {data_amanha.strftime('%d/%m/%Y')}).\n'  
                f'Caso não corresponda à esta mensagem, uma punição entrará em vigor.'
            )
            return render(request, 'denuncias/reuniao_selecionar.html', {'mensagem' : mensagem})
    
    else:
        form = ReuniaoForm()
    return render(request, 'denuncias/reuniao.html', {'form': form})


data_hoje = datetime.date.today()
data_amanha = data_hoje + timedelta(days=1)

def solicitar_tela(request):
    if request.method == 'POST':
        form = TelaForm(request.POST)
        
        if form.is_valid():
            pessoa = form.cleaned_data['escolha_var']
            acao = form.cleaned_data['escolha_acao']
            mensagem = (
                f'Boa noite, devido a sua ultima ação {acao.nome} procure o {pessoa.nome}, para enviar a gravação da tela completa e sem cortes.\n'  
            )
            return render(request, 'denuncias/tela_msg.html', {'mensagem' : mensagem})
    
    else:
        form = TelaForm()
    return render(request, 'denuncias/tela_criar.html', {'form': form})

