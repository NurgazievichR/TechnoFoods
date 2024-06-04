from rest_framework import routers
from django.urls import path

from apps.products.views import ProductAPIViewSet, CategoryProductsView, CategoryAPIView

router = routers.SimpleRouter()
router.register('products', ProductAPIViewSet)
router.register('categories', CategoryAPIView)

urlpatterns = router.urls

urlpatterns += [
    path('category_detail/<int:pk>', CategoryProductsView.as_view()),
]

