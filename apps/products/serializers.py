from rest_framework import serializers

from .models import Product, ProductParameter, Category, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductParameterSerialzier(serializers.ModelSerializer):
    class Meta:
        model = ProductParameter
        fields = ['key', 'value']

class ProductImageSerialzier(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image','color']


class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerialzier(many=True, read_only=True)
    product_parameters = ProductParameterSerialzier(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

