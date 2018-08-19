from universidades.models import Universidade
from universidades.serializers import UniversidadeSerializer
from rest_framework import permissions
from rest_framework import generics


# TODO: Add Campi list to
# UniversidadeList and UniversidadeDetail

class UniversidadeList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Universidade.objects.all()
    serializer_class = UniversidadeSerializer


class UniversidadeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Universidade.objects.all()
    serializer_class = UniversidadeSerializer


