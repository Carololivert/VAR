from django.urls import path
from .views import VAR_RegistroAPIView

urlpatterns = [
    # Esta é a URL que seu site Vue.js deve usar para enviar os dados
    path('api/cadastro/', VAR_RegistroAPIView.as_view(), name='api_var_cadastro'),
]