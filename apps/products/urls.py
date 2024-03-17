from rest_framework import routers

from apps.products.views import ProductAPIViewSet, CategoryAPIViewSet

router = routers.SimpleRouter()
router.register('products', ProductAPIViewSet)
router.register('category', CategoryAPIViewSet)

urlpatterns = router.urls