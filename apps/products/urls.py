from rest_framework import routers
from django.urls import path

from apps.products.views import ProductAPIViewSet, CategoryProductsView, CategoryAPIView

router = routers.SimpleRouter()
router.register('categories', CategoryAPIView)

urlpatterns = router.urls

urlpatterns += [
    path('category_detail/<int:pk>/', CategoryProductsView.as_view()),
    path('products/', ProductAPIViewSet.as_view({'get': 'list'}), name='product-list'),
    path('products/<slug:slug>/', ProductAPIViewSet.as_view({'get': 'retrieve'}), name='product-detail'),
]

