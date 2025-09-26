from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import CartItem
from .serializers import CartItemSerializer
class CartListCreateView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user).select_related('product')
    def perform_create(self, serializer):
        item, created = CartItem.objects.get_or_create(
            user=self.request.user,
            product=serializer.validated_data['product'],
            defaults={'quantity': serializer.validated_data.get('quantity',1)},
        )
        if not created:
            item.quantity += serializer.validated_data.get('quantity',1)
            item.save(update_fields=['quantity'])
    def list(self, request, *args, **kwargs):
        resp = super().list(request, *args, **kwargs)
        total = 0.0
        for i in self.get_queryset():
            total += float(i.product.price) * i.quantity
        resp.data = {'items': resp.data, 'total': f"{total:.2f}"}
        return resp
class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user).select_related('product')
