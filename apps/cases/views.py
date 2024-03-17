from rest_framework.viewsets import GenericViewSet, mixins

from .models import Case
from .serializers import CaseSerializer


class CasesViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

    