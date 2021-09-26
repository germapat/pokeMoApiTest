from pokemon.models import Pokemon
from fwbasemodel.rest.serializers import BaseModelSerializer


class PokemonSerializer(BaseModelSerializer):

    class Meta(BaseModelSerializer):
        model = Pokemon
        fields = ['name', 'base_stats', 'height', 'weight', 'evolutions', 'active', ]



