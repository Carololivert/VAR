from rest_framework import serializers
from .models import VAR_Registro

class VAR_RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = VAR_Registro
        # Cuidado aqui: 'criado_por' não está na lista
        # porque este campo será preenchido pela view, não pelo usuário.
        fields = ['nick_name', 'id_var', 'id_discord', 'motivo', 'tempo', 'link_evidencia']