
import json
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from pokemon.serializers import *
from pokemon.models import Pokemon as Pok
from pokemon.libs.poke_api import poke_api
from django.core.serializers import serialize
from django.http import JsonResponse
from django.db.models import Q



with open('pokeMoApi/pokeApi.json', 'r') as f:
    pokeApi = json.load(f)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class Pokemon(viewsets.ReadOnlyModelViewSet):
    queryset = Pok.objects.none()
    serializer_class = PokemonSerializer
    def get_service(request, **kwargs):

        if request.method == 'GET':
            if kwargs['pk'].isdigit():
                queryset =  Pok.objects.filter(id=kwargs['pk'])
            else:
                queryset =  Pok.objects.filter(name=kwargs['pk'])
            data = serialize("json", queryset)
            return JsonResponse({'result': data})


class Evolution(viewsets.ModelViewSet):
    search_fields = {'id'}
    def get_service(request, **kwargs):
        if kwargs['pk']:
            query = Pok.objects.filter(id=kwargs['pk'])
            # import pdb; pdb.set_trace()
            if not query:
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
            data = serialize("json", query)
            return JsonResponse({'result': data})
        return JsonResponse({'status': 404})
