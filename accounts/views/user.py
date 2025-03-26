from accounts.views.base import Base
from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

class GetUser(Base):
    authentication_classes = [JWTAuthentication]  # Adicionando autenticação JWT
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            # Obtém o usuário diretamente do request (já autenticado)
            user = request.user
            
            # Verificação adicional de segurança
            if not user.is_authenticated:
                return Response(
                    {"detail": "Usuário não autenticado"},
                    status=status.HTTP_401_UNAUTHORIZED
                )

            enterprise = self.get_enterprise_user(user.id)
            serializer = UserSerializer(user)

            return Response({
                "user": serializer.data,
                "enterprise": enterprise,
                # Adicionando informações úteis para debug
                "auth_status": "authenticated",
                "session_info": {
                    "token_valid": True,
                    "user_id": user.id
                }
            })

        except Exception as e:
            return Response(
                {"detail": "Erro ao obter informações do usuário", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )