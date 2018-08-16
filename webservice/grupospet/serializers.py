from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer

from django.contrib.auth.models import User
from userprofile.models import UserProfile
from django.contrib.auth import update_session_auth_hash

from grupospet.models import GrupoPet
from geolocalizacoes.models import Geolocalizacao
from geolocalizacoes.serializers import GeolocalizacaoSerializer

class GrupoPetSerializer(serializers.ModelSerializer):
    geolocalizacao = GeolocalizacaoSerializer(required=True)
    class Meta:
        model = GrupoPet
        fields = ('id', 'nome', 'area_do_conhecimento', 'interdisciplinar','membros', 'projetos', 'geolocalizacao')

    def create(self, validated_data):
        
        #TODO: Isso precisa ser refatorado
        # Nao ha garantias que geolocalizacao vai ser passado
        # Tambem eh necessario verificar se a geolocalizacao
        # ja existe no banco, devendo tornar (geo_lon,geo_lat) chave unica
        geolocalizacao_data = validated_data.pop('geolocalizacao')
        geolocalizacao = Geolocalizacao(**geolocalizacao_data)
        geolocalizacao.save()
        validated_data["geolocalizacao"] = geolocalizacao


        membros = validated_data.pop('membros')
        projetos = validated_data.pop('projetos')
        grupo = GrupoPet.objects.create(**validated_data)
        grupo.membros.set(membros)
        grupo.projetos.set(projetos)

        grupo.save()

        
        
        
        return grupo