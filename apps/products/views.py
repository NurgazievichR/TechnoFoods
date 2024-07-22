from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend


from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class ProductAPIViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'model', 'description', 'category__name']

    @method_decorator(cache_page(60*15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        slug = self.kwargs.get('slug')
        return queryset.get(slug=slug)


class CategoryAPIView(GenericViewSet, mixins.ListModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryProductsView(APIView):
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

    @method_decorator(cache_page(60*15))
    def get(self, request, pk):
        cat = get_object_or_404(Category, pk=pk)
        products = Product.objects.filter(category=pk)

        # Применение поиска
        search_query = request.query_params.get('search', None)
        if search_query:
            products = products.filter(
                Q(title__icontains=search_query) | 
                Q(model__icontains=search_query) | 
                Q(description__icontains=search_query)
            )

        #Создаем класс пагинатора, после из request берем offset и limit и нужное количество объектов возвращаем
        paginator = LimitOffsetPagination()
        paginated_products = paginator.paginate_queryset(products, request)

        serializer = ProductSerializer(paginated_products, many = True)
        return paginator.get_paginated_response({
            'title':cat.name,
            'products':serializer.data
        })