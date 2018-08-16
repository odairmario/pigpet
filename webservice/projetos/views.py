from projetos.models import Projeto
from projetos.serializers import ProjetoSerializer
from rest_framework import permissions
from rest_framework import generics


class ProjetoList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer


class ProjetoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer


