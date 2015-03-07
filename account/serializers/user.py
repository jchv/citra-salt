from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from account.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'display_name',
                  'personal_name', 'location', 'birth_date', 'gender',
                  'pronouns', 'is_staff', 'is_active', 'date_joined', 'url')
        read_only_fields = ('is_staff', 'is_active', 'date_joined')
        write_only_fields = ('password',)
        extra_kwargs = {
            'url': {'view_name': 'api:account:user-detail'}
        }

    def validate(self, attrs):
        attrs['password'] = make_password(attrs['password'])
        return attrs


class CredentialsSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        fields = ('username', 'password')
