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
    nick_name = models.ForeignKey(Vares, on_delete=models.CASCADE)
    id_punido = models.IntegerField("ID")
    id_dc = models.IntegerField('ID DC')
    motivo = models.ForeignKey(Motivo, on_delete=models.CASCADE)
    temp_ban = models.IntegerField("Tempo")
    link_evid = models.URLField("Link")
    created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f'{self.nick_name} , {self.motivo}, ({self.id_punido})'
    

