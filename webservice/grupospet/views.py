from grupospet.models import GrupoPet
from grupospet.serializers import GrupoPetSerializer
from rest_framework import permissions
from rest_framework import generics


class GrupoPetList(generics.ListCreateAPIView):
    queryset = GrupoPet.objects.all()
    serializer_class = GrupoPetSerializer


class GrupoPetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GrupoPet.objects.all()
    serializer_class = GrupoPetSerializer


