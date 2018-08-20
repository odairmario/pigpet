from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer

from django.contrib.auth.models import User
from userprofile.models import UserProfile
from django.contrib.auth import update_session_auth_hash

from campis.models import Campi
from geolocalizacoes.models import Geolocalizacao
from geolocalizacoes.serializers import GeolocalizacaoSerializer

class CampiSerializer(serializers.ModelSerializer):
    geolocalizacao = GeolocalizacaoSerializer(required=True)
    class Meta:
        model = Campi
        fields = ('id', 'nome', 'geolocalizacao','universidade','cidade')

    def create(self, validated_data):
        
        #TODO: Isso precisa ser refatorado
        # Nao ha garantias que geolocalizacao vai ser passado
        # Tambem eh necessario verificar se a geolocalizacao
        # ja existe no banco, devendo tornar (geo_lon,geo_lat) chave unica
        geolocalizacao_data = validated_data.pop('geolocalizacao')
        geolocalizacao = Geolocalizacao(**geolocalizacao_data)
        geolocalizacao.save()
        validated_data["geolocalizacao"] = geolocalizacao

        campi = Campi.objects.create(**validated_data)
        campi.save()
        
        return campi