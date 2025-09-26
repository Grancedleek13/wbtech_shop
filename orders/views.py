from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Order
from .serializers import OrderSerializer
from .services import create_order_from_cart, InsufficientStock, InsufficientBalance
class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related('items__product').order_by('-id')
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_from_cart(request):
    try:
        order = create_order_from_cart(request.user)
    except ValueError as e:
        return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except InsufficientStock as e:
        return Response({'detail': str(e)}, status=status.HTTP_409_CONFLICT)
    except InsufficientBalance as e:
        return Response({'detail': str(e)}, status=status.HTTP_402_PAYMENT_REQUIRED)
    return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
