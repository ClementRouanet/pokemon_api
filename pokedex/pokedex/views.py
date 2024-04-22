from django.http import JsonResponse
from django.db import connection

from .models import Move, Pokemon, Pokemon_Types, Types


def get_move_identifier(request, move_id):
    try :
        move = Move.objects.get(id=move_id)
        identifier = move.identifier
        return JsonResponse({'identifier ': identifier })
    
    except Move.DoesNotExist :
        return JsonResponse({'error': 'Move not found'}, status=404)
    


def get_pokemon_identifier(request, pokemon_id) :
    try :
        pokemon = Pokemon.objects.get(id=pokemon_id)
        identifier = pokemon.identifier
        return JsonResponse({'identifier ': identifier})
    
    except Pokemon.DoesNotExist :
        return JsonResponse({'error': 'Pokemon not found'}, status=404)
    


def get_pokemon_features(request, pokemon_name) :
    try :
        pokemon = Pokemon.objects.get(identifier=pokemon_name)

        identifier = pokemon.identifier
        height = pokemon.height
        weight = pokemon.weight
        base_experience = pokemon.base_experience

        return JsonResponse({'identifier ': identifier, 'height': height, 'weight': weight, 'base_experience': base_experience})
    
    except Pokemon.DoesNotExist :
        return JsonResponse({'error': 'Pokemon not found'}, status=404)



def get_pokemon_type(request, pokemon_name) :
    try :
        pokemon = Pokemon.objects.get(identifier=pokemon_name)
        pokemon_id = pokemon.id
    
        type = Pokemon_Types.objects.get(pokemon_id=pokemon_id)
        type_id = type.type_id

        type = Types.objects.get(type_id=type_id)
        pokemon_type = type.identifier

        return JsonResponse({'Pokemon ': pokemon_name, 'Type': pokemon_type})
    
    except Pokemon.DoesNotExist :
        return JsonResponse({'error': 'Pokemon Type not found'}, status=404)