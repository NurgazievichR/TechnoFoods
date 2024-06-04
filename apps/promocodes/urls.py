from rest_framework import routers
from django.urls import path


from .views import PromocodeViewSet, PromocodePlusView

router = routers.SimpleRouter()
router.register('', PromocodeViewSet)

urlpatterns = router.urls


urlpatterns += [
    path('plus/<int:pk>', PromocodePlusView.as_view()),
]