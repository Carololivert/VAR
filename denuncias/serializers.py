from rest_framework import serializers
from .models import Punições, Motivo, Vares, Acoes

# Serializer para o modelo Motivo (Usado para listagens e seleções)
class MotivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motivo
        fields = ['id', 'nome']

# Serializer para o modelo Vares (Usado para listagens e seleções de VARs)
class VaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vares
        fields = ['id', 'nome']

# Serializer para o modelo Acoes
class AcoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acoes
        fields = ['id', 'nome']

# Serializer principal para Punições (Onde as operações POST serão feitas)
class PunicoesSerializer(serializers.ModelSerializer):
    # Campos de leitura para exibir o NOME ao invés do ID de FK na resposta GET
    motivo_nome = serializers.CharField(source='motivo.nome', read_only=True)
    nick_name_nome = serializers.CharField(source='nick_name.nome', read_only=True)

    class Meta:
        model = Punições
        # Listamos os campos de FK (nick_name, motivo) para escrita/POST/PUT
        # E os campos de nome (nick_name_nome, motivo_nome) para leitura/GET
        fields = [
            'id', 
            'nick_name', 'nick_name_nome', # FK para Vares
            'id_punido', 
            'id_dc', 
            'motivo', 'motivo_nome',       # FK para Motivo
            'temp_ban', 
            'link_evid', 
            'created'
        ]
        
        # Opcional: Garante que os IDs grandes (como IDs de Discord) sejam tratados corretamente
        extra_kwargs = {
            'id_punido': {'min_value': 0},
            'id_dc': {'min_value': 0},
        }