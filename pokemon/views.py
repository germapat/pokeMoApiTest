
import json
from rest_framework import viewsets
from pokemon.serializers import *
from pokemon.models import Pokemon as Pok
from pokemon.libs.poke_api import poke_api
from django.core.serializers import serialize
from django.http import JsonResponse


with open('pokeMoApi/pokeApi.json', 'r') as f:
    pokeApi = json.load(f)


class Pokemon(viewsets.ReadOnlyModelViewSet):
    def get_pokemon(request, **kwargs):
        queryset = Pok.objects.filter(name=kwargs['name'])
        serializer = PokemonSerializer(queryset, many=True)
        return JsonResponse({'result': serializer.data})


class Evolution(viewsets.ReadOnlyModelViewSet):
    def get_service(request, **kwargs):
        if kwargs['pk']:
            queryset = Pok.objects.filter(id=int(kwargs['pk']))
            if not queryset:
                evolution = poke_api(pokeApi['evolution'] +  str(kwargs['pk']))
                if len(evolution) > 0:
                    name = evolution['chain']['species']['name']
                    evolution = evolution['chain']['evolves_to']
                    pokemon = poke_api(pokeApi['pokemon'] +  str(name))
                    height = pokemon['height']
                    weight = pokemon['weight']
                    id = pokemon['id']
                    pokemon_stats = pokemon['stats']
                    instance = Pok(evolutions=evolution, base_stats=pokemon_stats, height=height,
                                        weight=weight, id=id, name=name
                                      )
                    instance.save()
                    return JsonResponse({'result': {'name': name, 'height': height, 'weight': weight, 'id': id,
                                            'stats': pokemon_stats, 'evolution': evolution}}
                                        )
            data = PokemonSerializer(queryset, many=True)
            return JsonResponse({'result': data.data})
        return JsonResponse({'status': 404})
