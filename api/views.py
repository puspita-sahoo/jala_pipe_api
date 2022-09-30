from django.contrib.auth.models import User
from api.serializers import ProductSerializer, CartSerializer, CartProductSerializer
from .models import Product, Cart, CartProduct
from rest_framework import viewsets



# This class done work of create, retrieve, delete of product

class ProductAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartAPIView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartProductAPIView(viewsets.ModelViewSet):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer


