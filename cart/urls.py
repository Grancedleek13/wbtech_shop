from django.urls import path
from .views import CartListCreateView, CartItemDetailView
urlpatterns = [
    path('items/', CartListCreateView.as_view(), name='cart_items'),
    path('items/<int:pk>/', CartItemDetailView.as_view(), name='cart_item_detail'),
]
