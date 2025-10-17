from django.db import models

class Motivo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Vares(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Punições(models.Model):
    nick_name = models.ForeignKey(Vares, on_delete=models.CASCADE, verbose_name='Nome Var')
    id_punido = models.IntegerField("ID")
    id_dc = models.IntegerField('ID DC')
    motivo = models.ForeignKey(Motivo, on_delete=models.CASCADE)
    temp_ban = models.CharField(max_length=50, verbose_name="Tempo")
    link_evid = models.URLField("Link")
    created = models.DateTimeField(auto_now_add=True)
    codigo_tx = models.CharField(max_length=50, null=True, blank=True, verbose_name='Codigo-TX')

    
    def __str__(self):
        return f'{self.nick_name} , {self.motivo}, ({self.id_punido})'
    
class Acoes(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome}'
