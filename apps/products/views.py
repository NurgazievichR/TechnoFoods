from rest_framework.viewsets import mixins, GenericViewSet

from .models import Product
from .serializers import ProductSerializer

class ProductAPIViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

