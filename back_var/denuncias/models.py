from django.db import models

from django.conf import settings

class VAR_Registro(models.Model):
    nick_name = models.CharField(max_length=100)
    id_denunciado = models.CharField(max_length=50)
    id_discord = models.CharField(max_length=50)
    motivo = models.CharField(max_length=50)
    tempo = models.CharField(max_length=20)
    link_evidencia = models.URLField(max_length=200, blank=True, null=True)

    data_criacao = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Registro: {self.nick_name}, Denuncia: {self.motivo}"