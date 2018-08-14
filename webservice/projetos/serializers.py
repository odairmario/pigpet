from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer

from django.contrib.auth.models import User
from userprofile.models import UserProfile
from django.contrib.auth import update_session_auth_hash

from projetos.models import Projeto
from grupospet.models import GrupoPet

class ProjetoSerializer(serializers.ModelSerializer):
    grupos_pet = serializers.HyperlinkedRelatedField(many=True, view_name='grupospet-detail', queryset=GrupoPet.objects.all())
    class Meta:
        model = Projeto
        fields = ('id', 'nome', 'descricao', 'texto','ativo', 'membros', 'grupos_pet')