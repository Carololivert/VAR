from django.test import TestCase

from django.test import TestCase
# Importamos todos os modelos que vamos testar
from .models import Motivo, Vares, Punições, Acoes

class MotivoModelTest(TestCase):
    def test_motivo_creation(self):
        # Testar se um objeto Motivo é criado corretamente
        motivo = Motivo.objects.create(nome='Uso de Hacks')
        self.assertEqual(motivo.nome, 'Uso de Hacks')
        self.assertTrue(isinstance(motivo, Motivo))

    def test_motivo_str_representation(self):
        # Testar o método __str__
        motivo = Motivo.objects.create(nome='Comportamento Tóxico')
        self.assertEqual(str(motivo), 'Comportamento Tóxico')


class AcoesModelTest(TestCase):
    def test_acao_creation(self):
        # Testar se um objeto Acoes é criado corretamente
        acao = Acoes.objects.create(nome='Banimento Permanente')
        self.assertEqual(acao.nome, 'Banimento Permanente')

    def test_acao_str_representation(self):
        # Testar o método __str__
        acao = Acoes.objects.create(nome='Mute')
        self.assertEqual(str(acao), 'Mute')

class VaresModelTest(TestCase):
    def test_vares_creation(self):
        # Testar se um objeto Vares é criado corretamente
        jogador = Vares.objects.create(nome='PlayerXpto')
        self.assertEqual(jogador.nome, 'PlayerXpto')

    def test_vares_str_representation(self):
        # Testar o método __str__
        jogador = Vares.objects.create(nome='ModeradorZ')
        self.assertEqual(str(jogador), 'ModeradorZ')

class PunicoesModelTest(TestCase):
    def setUp(self):
        # 1. Configuração: Criar instâncias necessárias para o teste de Punições
        self.jogador = Vares.objects.create(nome='GuerreiroDelta')
        self.motivo = Motivo.objects.create(nome='Abuso de Bug')

    def test_punicao_creation(self):
        # 2. Testar a criação do objeto Punição
        punicao = Punições.objects.create(
            nick_name=self.jogador,
            id_punido=12345,
            id_dc=987654321,
            motivo=self.motivo,
            temp_ban=7,  # 7 dias
            link_evid='http://link.para.evidencia.com/123'
        )
        
        # Verificar se as chaves estrangeiras foram relacionadas corretamente
        self.assertEqual(punicao.nick_name, self.jogador)
        self.assertEqual(punicao.motivo, self.motivo)
        
        # Verificar o valor dos campos
        self.assertEqual(punicao.id_punido, 12345)
        self.assertEqual(punicao.temp_ban, 7)
        self.assertTrue('http://' in punicao.link_evid)
        
        # Verificar se o campo 'created' foi preenchido automaticamente
        self.assertIsNotNone(punicao.created)

    def test_punicao_str_representation(self):
        # 3. Testar o método __str__
        punicao = Punições.objects.create(
            nick_name=self.jogador,
            id_punido=54321,
            id_dc=123456789,
            motivo=self.motivo,
            temp_ban=30,
            link_evid='http://teste.com'
        )
        
        # O __str__ deve ser: 'nick_name , motivo, (id_punido)'
        expected_str = f'{self.jogador.nome} , {self.motivo.nome}, ({punicao.id_punido})'
        self.assertEqual(str(punicao), expected_str)