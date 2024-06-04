from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class ProductAPIViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryAPIView(GenericViewSet, mixins.ListModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryProductsView(APIView):
    def get(self, request, pk):
        lst = ProductSerializer(Product.objects.filter(category=pk), many=True)
        cat = get_object_or_404(Category, pk=pk)

        return Response({'title':cat.name, 'products':lst.data})