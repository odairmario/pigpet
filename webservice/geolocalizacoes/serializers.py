from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer

from django.contrib.auth.models import User
from userprofile.models import UserProfile
from django.contrib.auth import update_session_auth_hash

from geolocalizacoes.models import Geolocalizacao

class GeolocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocalizacao
        fields = ('id', 'geo_lat', 'geo_lon')