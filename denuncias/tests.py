from django.test import TestCase, Client
from django.urls import reverse
from .models import Motivo, Vares, Punições, Acoes

class DenunciasTests(TestCase):
    """
    Conjunto de testes para os modelos e views da aplicação 'denuncias'.
    """
    def setUp(self):
        """Configuração inicial para criar objetos de teste no banco de dados."""
        self.client = Client()
        
        # 1. Criação de Modelos base (necessários para as chaves estrangeiras)
        self.var_teste = Vares.objects.create(nome='VarTestador')
        self.motivo_teste = Motivo.objects.create(nome='RDM - Regra de Mata')
        self.acao_teste = Acoes.objects.create(nome='Tentativa de Voo')
        
        # 2. Dados válidos para Formulários
        self.punicao_data = {
            # Usamos o ID dos objetos de teste
            'nick_name': self.var_teste.id, 
            'id_punido': 12345,
            'id_dc': 67890,
            'motivo': self.motivo_teste.id,
            'temp_ban': 7,
            'link_evid': 'https://link.teste/punicao_rdm'
        }
        
        self.var_data = {
            'nome': 'NovoVAR'
        }
        
        # 3. Nomes de URLs (usando reverse() para segurança)
        self.punicao_url = reverse('criar_punicao')
        self.var_url = reverse('var')
        self.reuniao_url = reverse('chamar_reuniao')
        self.tela_url = reverse('solicitar_tela')
        self.vares_list_url = reverse('exibir_vares')


    # ---------------------------------------------
    # Testes de Modelo (__str__ e criação)
    # ---------------------------------------------
    
    def test_motivo_model_str(self):
        """Verifica se o __str__ do modelo Motivo retorna o nome correto."""
        motivo = Motivo.objects.get(id=self.motivo_teste.id)
        self.assertEqual(str(motivo), 'RDM - Regra de Mata')
        
    def test_vares_model_str(self):
        """Verifica se o __str__ do modelo Vares retorna o nome correto."""
        var = Vares.objects.get(id=self.var_teste.id)
        self.assertEqual(str(var), 'VarTestador')
        
    def test_punicao_model_str(self):
        """Verifica se o __str__ do modelo Punições retorna o formato esperado."""
        punicao = Punições.objects.create(**self.punicao_data)
        # O formato é: '{self.nick_name} , {self.motivo}, ({self.id_punido})'
        expected_str = f'{self.var_teste.nome} , {self.motivo_teste.nome}, ({self.punicao_data["id_punido"]})'
        self.assertEqual(str(punicao), expected_str)


    # ---------------------------------------------
    # Testes de Views (GET - Renderização)
    # ---------------------------------------------

    def test_criar_punicao_view_get(self):
        """Testa se a página de criação de punição carrega com sucesso."""
        response = self.client.get(self.punicao_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'denuncias/criar_punicao.html')

    def test_exibir_vares_view_get(self):
        """Testa se a página de listagem de vares carrega e exibe o var de teste."""
        response = self.client.get(self.vares_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'denuncias/exibir_vares.html')
        self.assertContains(response, self.var_teste.nome) 


    # ---------------------------------------------
    # Testes de Views (POST - Criação e Lógica)
    # ---------------------------------------------

    def test_criar_punicao_view_post_success(self):
        """Testa a criação de uma punição com dados válidos."""
        response = self.client.post(self.punicao_url, data=self.punicao_data)
        
        # Verifica se um objeto Punições foi criado no banco
        self.assertTrue(Punições.objects.exists())
        punicao_criada = Punições.objects.get(id_punido=12345)
        self.assertEqual(punicao_criada.temp_ban, 7)

        # Verifica a renderização do template de sucesso e o conteúdo da mensagem
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'denuncias/punicao_sucesso.html')
        self.assertContains(response, 'ID: 12345') 
        self.assertContains(response, self.motivo_teste.nome) 

    def test_criar_var_view_post_success(self):
        """Testa a criação de um novo VAR e o redirecionamento para a página de sucesso dedicada."""
        response = self.client.post(self.var_url, data=self.var_data)
        
        # Verifica se o objeto Vares foi criado no banco
        self.assertEqual(Vares.objects.count(), 2) # 1 do setUp + 1 novo
        self.assertTrue(Vares.objects.filter(nome='NovoVAR').exists())

        # Verifica a renderização do template var_sucesso.html
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'denuncias/var_sucesso.html')
        self.assertContains(response, 'VAR NovoVAR foi salvo com sucesso')

    def test_chamar_reuniao_view_post_success(self):
        """Testa a geração da mensagem de reunião."""
        reuniao_data = {
            'escolha_var': self.var_teste.id 
        }
        response = self.client.post(self.reuniao_url, data=reuniao_data)
        
        # Verifica o template de mensagem e o nome do VAR na mensagem
        self.assertTemplateUsed(response, 'denuncias/reuniao_selecionar.html')
        self.assertContains(response, f'Procure o {self.var_teste.nome}, para agendar um horário')

    def test_solicitar_tela_view_post_success(self):
        """Testa a geração da mensagem de solicitação de tela."""
        tela_data = {
            'escolha_var': self.var_teste.id, 
            'escolha_acao': self.acao_teste.id
        }
        response = self.client.post(self.tela_url, data=tela_data)
        
        # Verifica o template de mensagem e os dados na mensagem
        self.assertTemplateUsed(response, 'denuncias/tela_msg.html')
        self.assertContains(response, f'sua ultima ação {self.acao_teste.nome} procure o {self.var_teste.nome}')