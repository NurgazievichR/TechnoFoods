from rest_framework import routers

from apps.products.views import ProductAPIViewSet

router = routers.DefaultRouter()
router.register('products', ProductAPIViewSet)

urlpatterns = router.urls