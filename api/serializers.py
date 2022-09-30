from rest_framework import serializers
from .models import Product, Cart, CartProduct



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = "__all__"











# class SizeViewSet(viewsets.ModelViewSet):
#     queryset = models.Size.objects.all()
#     serializer_class = SizeSerializer

# class ProductVariantSerializer(serializers.ModelSerializer):
#     product = serializers.PrimaryKeyRelatedField(
#         queryset=models.Product.objects.all())
#     size = serializers.PrimaryKeyRelatedField(
#         queryset=models.Size.objects.all())
#     class Meta:
#         model = models.ProductVariant
#         fields = ('id', 'product', 'size')
#         read_only_fields = ('id',)


# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = models.Product.objects.all()
#     serializer_class = ProductSerializer
















