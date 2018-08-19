from campis.models import Campi
from campis.serializers import CampiSerializer
from rest_framework import permissions
from rest_framework import generics


class CampiList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Campi.objects.all()
    serializer_class = CampiSerializer


class CampiDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Campi.objects.all()
    serializer_class = CampiSerializer


