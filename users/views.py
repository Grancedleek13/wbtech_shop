from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, ProfileSerializer, TopUpSerializer
User = get_user_model()
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    def get_object(self): return self.request.user
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def top_up(request):
    s = TopUpSerializer(data=request.data); s.is_valid(raise_exception=True)
    amount = s.validated_data['amount']; u = request.user
    u.balance += amount; u.save(update_fields=['balance'])
    return Response({'balance': str(u.balance)})
