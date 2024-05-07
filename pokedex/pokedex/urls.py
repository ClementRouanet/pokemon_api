"""
URL configuration for pokedex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import *


urlpatterns = [
    # Récupère le nom du mouvement en fonction de l'id entré dans l'url
    path('api/moves/<int:move_id>/', get_move_identifier, name='get_move_identifier'),

    # Récupère le nom du pokemon en fonction de l'id entré dans l'url
    path('api/pokemon/<int:pokemon_id>/', get_pokemon_identifier, name='get_pokemon_identifier'),

    # Récupère le nom la hauteur, le poids et l'expérience de base en fonction du nom du pokemon entré dans l'url
    path('api/pokemon/<str:pokemon_name>/', get_pokemon_features, name='get_pokemon_features'),

    # Récupère le le type en fonction du nom du pokemon entré dans l'url
    path('api/pokemon/types/<str:pokemon_name>/', get_pokemon_type, name='get_pokemon_type'),

    # Récupère le nom de l'item en fonction de l'id entré dans l'url
    path('api/items/<int:item_id>/', get_item_identifier, name='get_item_identifier'),

    # Permet à un utilisateur de se connecter et avoir un token pour un pseudo et mot de passe valide
    path('api/connexion/', connexion, name='connexion'),

    # Permet à un utilisateur de se créer un user avec un pokedex vide
    path('api/register/', register, name='register'),

    # Permet à un utilisateur authentifié d'accéder à son pokedex (liste de pokemons)
    path('api/mesPokemons/', get_pokemons_in_bag, name='get_pokemons_in_bag'),

    # Permet à un utilisateur authentifié d'ajouter un ou plusieurs pokemon(s) à son pokedex
    path('api/addPokemons/', add_pokemons_in_bag, name='add_pokemons_in_bag'),

    # Permet à un utilisateur authentifié de supprimer un ou plusieurs pokemon(s) à son pokedex
    path('api/remPokemons/', rem_pokemons_in_bag, name='rem_pokemons_in_bag'),

    # Permet à un admin authentifié de récupérer le rôle de tout le monde (users + admins)
    path('api/role/', get_users_role, name='get_users_role'),

    # Permet à un admin authentifié de modifier le rôle à un user (admin -> user  ou  user -> admin)
    path('api/admin/users/', update_users_role, name='update_users_role'),
]