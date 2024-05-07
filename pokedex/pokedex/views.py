from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Move, Pokemon, Pokemon_Types, Types, Item, User, Bag
from .utils import generate_jwt_token, authenticate_user, token_validation, is_admin



# Fonction qui récupère le nom du mouvement en fonction de l'id entré dans l'url
def get_move_identifier(request, move_id):
    try :
        move = Move.objects.get(id=move_id)
        identifier = move.identifier
        return JsonResponse({'identifier ': identifier })
    
    except Move.DoesNotExist :
        return JsonResponse({'error': 'Move not found'}, status=404)
    


# Fonction qui récupère le nom du pokemon en fonction de l'id entré dans l'url
def get_pokemon_identifier(request, pokemon_id) :
    try :
        pokemon = Pokemon.objects.get(id=pokemon_id)
        identifier = pokemon.identifier
        return JsonResponse({'identifier ': identifier})
    
    except Pokemon.DoesNotExist :
        return JsonResponse({'error': 'Pokemon not found'}, status=404)
    


# Fonction qui récupère le nom la hauteur, le poids et l'expérience de base en fonction du nom du pokemon entré dans l'url
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



# Fonction qui récupère le le type en fonction du nom du pokemon entré dans l'url
def get_pokemon_type(request, pokemon_name) :
    try :
        pokemon = Pokemon.objects.get(identifier=pokemon_name)
        pokemon_id = pokemon.id
        
        pokemon_type = Pokemon_Types.objects.filter(pokemon_id=pokemon_id).first()
        type_id = pokemon_type.type_id

        if pokemon_type :
            type_of_pokemon = Types.objects.get(id=type_id)
            type_of_pokemon = type_of_pokemon.identifier
            return JsonResponse({'Pokemon': pokemon_name, 'Type': type_of_pokemon})
        else :
            return JsonResponse({'error': 'Pokemon type not found'}, status=404)
    
    except Pokemon.DoesNotExist :
        return JsonResponse({'error': 'Pokemon not found'}, status=404)
    
    except Types.DoesNotExist :
        return JsonResponse({'error': 'Type not found'}, status=404)
    


# Fonction qui récupère le nom de l'item en fonction de l'id entré dans l'url
def get_item_identifier(request, item_id) :
    try:
        item = Item.objects.get(id=item_id)
        data = {
            'Identifier': item.identifier
        }
        return JsonResponse(data)
    except Move.DoesNotExist :
        return JsonResponse({'error': 'Item not found'}, status=404)
    


# Fonction qui permet à un utilisateur de se connecter et avoir un token pour un pseudo et mot de passe valide
@csrf_exempt
def connexion(request) :
    if request.method == 'POST' :
        data = json.loads(request.body.decode('utf-8'))

        username = data['username']
        password = data['password']

        user = authenticate_user(username, password)

        if user :
            token = generate_jwt_token(user.id)
            return JsonResponse({'token': token})
        else :
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
    else :
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    


# Fonction qui permet à un utilisateur de se créer un user avec un pokedex vide
@csrf_exempt
def register(request) :
    if request.method == 'POST' :
        data = json.loads(request.body.decode('utf-8'))

        pseudo = data.get('username')
        password = data.get('password')
        role = data.get('role')

        # Vérifier si les champs nécessaires sont fournis
        if not pseudo or not password :
            return JsonResponse({'error': 'Le pseudo et le mot de passe sont requis'}, status=400)
        
        # Vérifier si l'utilisateur est déjà pris
        if User.objects.filter(pseudo=pseudo).exists() :
            return JsonResponse({'error': 'UserName already used'}, status=405)

        # Créer un nouvel utilisateur
        try :
            if role :
                User().create_user(pseudo=pseudo, password=password, role=role)
            else :
                User().create_user(pseudo=pseudo, password=password)

            return JsonResponse({'success': 'User created successfully'}, status=201)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Method not allowed'}, status=405)



# Fonction qui permet à un utilisateur authentifié d'accéder à son pokedex (liste de pokemons)
def get_pokemons_in_bag(request) :
    answer, user_id = token_validation(request)

    if answer == True :
        bag_pokemons = Bag.objects.filter(user_id=user_id)
        pokemon_ids = [pokemon.pokemon_id for pokemon in bag_pokemons]

        pokemon_list = []
        for pokemon_id in pokemon_ids :
            pokemon = Pokemon.objects.get(id=pokemon_id)
            pokemon_list.append(pokemon.identifier)

        pokemons = dict(zip(pokemon_ids, pokemon_list))

        return JsonResponse({'My pokemons': pokemons})
    
    else :
        return answer
    


# Fonction qui permet à un utilisateur authentifié d'ajouter un ou plusieurs pokemon(s) à son pokedex
@csrf_exempt
def add_pokemons_in_bag(request) :
    answer, user_id = token_validation(request)

    if request.method == 'POST' :
        if answer == True :
            data = json.loads(request.body.decode('utf-8'))
            pokemon_ids = data.get('pokemons', [])
            
            for pokemon_id in pokemon_ids:
                if Bag.objects.filter(user_id=user_id, pokemon_id=pokemon_id).exists():
                    print("Le Pokémon avec l'ID {} est déjà dans le sac de l'utilisateur.".format(pokemon_id))
                else:
                    Bag.objects.create(user_id=user_id, pokemon_id=pokemon_id)

            return JsonResponse({'success': 'Pokemons added successfully'}, status=200)

        else :
            return answer



# Fonction qui permet à un utilisateur authentifié de supprimer un ou plusieurs pokemon(s) à son pokedex
@csrf_exempt
def rem_pokemons_in_bag(request) :
    answer, user_id = token_validation(request)

    if request.method == 'DELETE' :
        if answer == True :
            data = json.loads(request.body.decode('utf-8'))
            pokemon_ids = data.get('pokemons', [])
            
            for pokemon_id in pokemon_ids:
                pokemon = Bag.objects.filter(user_id=user_id, pokemon_id=pokemon_id)

                if pokemon:
                    pokemon.delete()
                else:
                    print("Le Pokémon avec l'ID {} n'est pas présent dans le sac de l'utilisateur.".format(pokemon_id))

            return JsonResponse({'success': 'Pokemons removed successfully'}, status=200)

        else :
            return answer
        


# Fonction qui permet à un admin authentifié de récupérer le rôle de tout le monde (users + admins)
def get_users_role(request) :
    answer, user_id = token_validation(request)

    if is_admin(user_id) :
        if answer == True :
            users = User.objects.all()

            pseudos = []
            roles = []

            for user in users :
                pseudos.append(user.pseudo)
                roles.append(user.role)

            users_roles = dict(zip(pseudos, roles))

            return JsonResponse({'User roles': users_roles})
        
        else :
            return answer
        
    else :
        return JsonResponse({'error': "User is not admin"})
    


# Fonction qui permet à un admin authentifié de modifier le rôle à un user (admin -> user  ou  user -> admin)
@csrf_exempt
def update_users_role(request) :
    answer, user_id = token_validation(request)

    if answer == True :
        if is_admin(user_id) :
            data = json.loads(request.body.decode('utf-8'))

            pseudo = data.get('username')
            role = data.get('role')

            user = User.objects.get(pseudo=pseudo)
            user.role = role
            user.save()

            return JsonResponse({'success': f"{pseudo} role updated to {role}"})
        
        else :
            return JsonResponse({'error': "User is not admin"})
        
    else :
        return answer
