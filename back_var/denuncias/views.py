from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import VAR_RegistroSerializer

User = get_user_model()

class VAR_RegistroAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Pega os dados enviados pelo front-end
        serializer = VAR_RegistroSerializer(data=request.data)
        
        # O Django valida se os dados do formulário são válidos
        if serializer.is_valid():
            # Pega o user_id que o front-end deve enviar
            user_id = request.data.get('user_id')
            
            if user_id:
                try:
                    # Encontra o usuário no banco de dados usando o ID
                    user_instance = User.objects.get(id=user_id)
                    
                    # Salva o registro no banco, associando-o ao usuário encontrado
                    serializer.save(criado_por=user_instance)
                    
                    # Retorna uma resposta de sucesso
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                except User.DoesNotExist:
                    # Retorna um erro se o ID de usuário não existir
                    return Response({"erro": "ID de usuário inválido."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # Retorna um erro se o ID não for enviado
                return Response({"erro": "O 'user_id' é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Retorna os erros de validação do formulário, se houver
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)