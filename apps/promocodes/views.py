from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


from .models import Promocode
from .serializers import PromocodeSerializer


class PromocodeViewSet(ReadOnlyModelViewSet):
    queryset = Promocode.objects.all()
    serializer_class = PromocodeSerializer



class PromocodePlusView(APIView):
    def patch(self, request, pk):
        pr = (get_object_or_404(Promocode, pk=pk))
        pr.used+=1
        pr.save()
        promocode = PromocodeSerializer(pr)

        return Response({'promocode':promocode.data})