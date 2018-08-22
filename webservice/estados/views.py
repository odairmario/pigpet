from estados.models import Estado
from estados.serializers import EstadoSerializer
from rest_framework import permissions
from rest_framework import generics


# TODO: Add Campi list to
# UniversidadeList and UniversidadeDetail

class EstadoList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer


class EstadoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer


