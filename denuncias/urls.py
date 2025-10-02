from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter # NOVO: Importando o router

router = DefaultRouter()
router.register(r'punicoes', views.PunicoesViewSet)
router.register(r'motivos', views.MotivoViewSet)
router.register(r'vares', views.VaresViewSet)
router.register(r'acoes', views.AcoesViewSet)


urlpatterns = [
    path('', views.criar_punicao, name='criar_punicao'),
    path('creat/', views.criar_var, name='var'),
    path('vares/', views.exibir_vares, name='exibir_vares'),
    path('reuniao/',views.chamar_reuniao, name='chamar_reuniao'),
    path('tela/',views.solicitar_tela, name='solicitar_tela'),
    path('historico/', views.exibir_historico, name='exibir_historico'),
    path('api/', include(router.urls)),
]