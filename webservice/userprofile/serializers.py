from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer

from django.contrib.auth.models import User
from userprofile.models import UserProfile
from django.contrib.auth import update_session_auth_hash

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        read_only_fields = ('created_at', 'updated_at',)
        fields = ('phone', 'cell_phone', 'active', 'userType', 'created_at', 'updated_at')


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = (
            'username','id', 'email', 'first_name', 'last_name', 'password', 'profile',
        )

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()

        userProfile = UserProfile(**profile_data)
        userProfile.username = user.username
        userProfile.user = user
        userProfile.save()
        
        
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        # Update User data
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('first_name', instance.email)
        # Update UserProfile data
        if not instance.profile:
            UserProfile.objects.create(user=instance, **profile_data)
        instance.profile.uid = profile_data.get('uid', instance.profile.uid)
        instance.profile.phone = profile_data.get('uid', instance.profile.phone)
        instance.profile.cell_phone = profile_data.get('uid', instance.profile.cell_phone)
        instance.save()
        # Check if the password has changed
        password = validated_data.get('password', None)

        if password:
            instance.set_password(password)
            instance.save()
            update_session_auth_hash(self.context.get('request'), instance)

        return instance
