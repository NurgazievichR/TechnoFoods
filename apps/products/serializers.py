from rest_framework import serializers

from .models import Product, ProductParameter, Category


class ProductParameterSerialzier(serializers.ModelSerializer):
    class Meta:
        model = ProductParameter
        fields = ['key', 'value']


class ProductSerializer(serializers.ModelSerializer):
    product_parameters = ProductParameterSerialzier(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    productsOfCategory = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'
