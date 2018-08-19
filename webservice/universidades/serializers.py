from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer

from django.contrib.auth.models import User
from userprofile.models import UserProfile
from django.contrib.auth import update_session_auth_hash

from universidades.models import Universidade
from campis.models import Campi
from campis.serializers import CampiSerializer

class UniversidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidade
        fields = ('id', 'nome','sigla')