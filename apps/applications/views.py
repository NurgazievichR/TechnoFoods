from rest_framework.viewsets import GenericViewSet, mixins

from .models import Application
from .serializers import ApplicationSeriazlier

class ApplicationViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Application
    serializer_class = ApplicationSeriazlier