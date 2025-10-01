from django.urls import path
from . import views

urlpatterns = [
    path('', views.criar_punicao, name='criar_punicao'),
    path('creat/', views.criar_var, name='var'),
    path('vares/', views.exibir_vares, name='exibir_vares'),
    path('reuniao/',views.chamar_reuniao, name='chamar_reuniao'),
    path('tela/',views.solicitar_tela, name='solicitar_tela'),
    path('historico/', views.exibir_historico, name='exibir_historico'),
]