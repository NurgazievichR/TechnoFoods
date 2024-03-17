from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product, Category
from .serializers import ProductSerializer

class ProductAPIViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryProductsView(APIView):
    def get(self, request, pk):
        lst = ProductSerializer(Product.objects.filter(category=pk), many=True)
        cat = get_object_or_404(Category, pk=pk)

        for product_data in lst.data:
            product_data['image'] = request.build_absolute_uri(product_data['image'])
        
        return Response({'title':cat.name, 'products':lst.data})
