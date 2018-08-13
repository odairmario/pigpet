from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer

from django.contrib.auth.models import User
from userprofile.models import UserProfile
from django.contrib.auth import update_session_auth_hash

from grupospet.models import GrupoPet

class GrupoPetSerializer(serializers.ModelSerializer):
    membros = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='userprofile-detail')

    class Meta:
        model = GrupoPet
        fields = ('id', 'nome', 'area_do_conhecimento', 'interdisciplinar','membros')