from rest_framework.viewsets import mixins, GenericViewSet

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class ProductAPIViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CategoryAPIViewSet(GenericViewSet, mixins.RetrieveModelMixin,):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
