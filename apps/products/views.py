from rest_framework.viewsets import mixins, GenericViewSet

from .models import Product, Category
from .serializers import ProductSerializer

class ProductAPIViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CategoryAPIViewSet(GenericViewSet, mixins.RetrieveModelMixin,):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        q = Product.objects.filter(category=self.kwargs['pk'])
        return q
