from rest_framework import routers

from .views import CasesViewSet

router = routers.SimpleRouter()
router.register('', CasesViewSet)