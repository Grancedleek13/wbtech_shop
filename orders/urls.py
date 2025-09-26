from django.urls import path
from .views import OrderListView, create_from_cart
urlpatterns = [
    path('', OrderListView.as_view(), name='orders'),
    path('create-from-cart/', create_from_cart, name='create_from_cart'),
]
