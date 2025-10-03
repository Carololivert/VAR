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


            id_punido = punicao_salva.id_punido
            motivo_id = punicao_salva.motivo.id
            
            punicoes_anteriores_mesmo_motivo = Punições.objects.filter(
                id_punido=id_punido,
                motivo_id=motivo_id
            ).exclude(pk=punicao_salva.pk)
            
            count_mesmo_motivo = punicoes_anteriores_mesmo_motivo.count()

            ultima_punicao = Punições.objects.filter(id_punido=id_punido).order_by('-created').exclude(pk=punicao_salva.pk).first()
            
            
            alerta_historico = None
            if count_mesmo_motivo > 0:

                vez = count_mesmo_motivo + 1
                alerta_historico = f'ALERTA DE REINCIDÊNCIA: Este ID já foi punido {count_mesmo_motivo} vez(es) por "{punicao_salva.motivo.nome}". Esta é a {vez}ª ocorrência.'
            
            data_ultima_punicao = None
            motivo_ultima_punicao = None

            if ultima_punicao:
                data_ultima_punicao = ultima_punicao.created.strftime("%d/%m/%Y às %H:%M")
                motivo_ultima_punicao = ultima_punicao.motivo.nome

            nome_tempo = ['Indeterminado'] 
            nome_formatado = punicao_salva.temp_ban.strip().lower()

            if nome_formatado in [n.lower() for n in nome_tempo]:
                usar_dias = '' 
            else:
                usar_dias = 'dias'


            mensagem = (
                f'**ID:** {punicao_salva.id_punido}\n'
                f'**ID Discord:** {punicao_salva.id_dc}\n'
                f'**Motivo:** {punicao_salva.motivo.nome}\n'
                f'**Tempo:** {punicao_salva.temp_ban} {usar_dias}\n'
                f'**Provas:** {punicao_salva.link_evid}\n'
                f'**Codigo-TX:** {punicao_salva.codigo_tx}\n'
            )

            msg = ( 
                f'Sua allowlist está sendo removida por {punicao_salva.temp_ban} dias, por conduta inadequada no Complexo XP.\n'
                f'Segue nossa análise: {punicao_salva.motivo.nome}'
            )
            contexto = {
                'mensagem' : mensagem,
                'msg' : msg,
                'alerta_historico': alerta_historico, 
                'data_ultima_punicao': data_ultima_punicao, 
                'motivo_ultima_punicao': motivo_ultima_punicao,
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

            nomes_femininos = ['carolzinha', 'rezinha'] 
            nome_formatado = pessoa.nome.strip().lower()

            if nome_formatado in [n.lower() for n in nomes_femininos]:
                pronome_artigo = 'a' 
            else:
                pronome_artigo = 'o'
        
            mensagem = (
                f'{saudacao}, você está sendo convidado(a) a participar de uma reunião com a Administração. Procure {pronome_artigo} {pessoa.nome}, para agendar um horário, na data de hoje ou amanhã ({data_hoje.strftime('%d/%m/%Y')} ou {data_amanha.strftime('%d/%m/%Y')}).\n'  
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

            nomes_femininos = ['carolzinha', 'rezinha'] 
            nome_formatado = pessoa.nome.strip().lower()

            if nome_formatado in [n.lower() for n in nomes_femininos]:
                pronome_artigo = 'a' 
            else:
                pronome_artigo = 'o'
            mensagem = (
                f'{saudacao}, devido a sua ultima ação {acao.nome} procure {pronome_artigo} {pessoa.nome}, para enviar a gravação da tela completa e sem cortes.\n'  
            )
            return render(request, 'denuncias/tela_msg.html', {'mensagem' : mensagem})
    
    else:
        form = TelaForm()
    return render(request, 'denuncias/tela_criar.html', {'form': form})

hora_atual = datetime.datetime.now().hour
saudacao = ''

if hora_atual < 12:
    saudacao = 'Bom dia'
elif hora_atual < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'


def exibir_historico(request):
    historico_punicoes = Punições.objects.all().order_by('-created')
    contexto = {'historico_punicoes': historico_punicoes}
    return render(request,'denuncias/historico.html', contexto)

def conta_punicoes(request):
    total_punicoes = Punições.objects.count()
    contexto = {"total_punicoes" : total_punicoes}
    return render(request, 'denuncias/cria_punicao.html', contexto)
