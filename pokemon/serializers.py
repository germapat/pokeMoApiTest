from django.contrib.auth.models import User, Group
from rest_framework import serializers
from pokemon.models import Pokemon
from fwbasemodel.rest.serializers import BaseModelSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']




class PokemonSerializer(BaseModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='pokemon-detail', read_only=True)

    class Meta:
        model = Pokemon
        fields = ['url', 'name', 'base_stats', 'height', 'weight', 'evolutions', 'created_at', 'active']
        read_only_fieds = ('url',)

