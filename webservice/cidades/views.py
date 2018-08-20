from cidades.models import Cidade
from cidades.serializers import CidadeSerializer
from rest_framework import permissions
from rest_framework import generics


# TODO: Add Campi list to
# UniversidadeList and UniversidadeDetail

class CidadeList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer


class CidadeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer


