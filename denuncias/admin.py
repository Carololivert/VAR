from django.contrib import admin
from .models import Motivo, Punições, Vares, Acoes


class PunicoesAdmin(admin.ModelAdmin):
    # Campos que devem ser exibidos na tela de lista
    list_display = ('nick_name', 'motivo', 'id_punido','id_dc', 'created') 
    
    readonly_fields = ('created','nick_name') 

admin.site.register(Motivo)
admin.site.register(Punições, PunicoesAdmin)
admin.site.register(Vares)
admin.site.register(Acoes)
