#              API et Web Services   -   Projet Pokedex  
  

Réalisé par HOUKMI Salaheddine & ROUANET Clément  
M2 Data Engineering & AI  -  EFREI Paris  


## Création de la DataBase :
 Exécuter les deux scripts SQL : **pokedex.sql** et **Create User and Bag Tables.sql**  


## Lancement du programme :
 Se placer dans le chemin : **/pokemon_api/pokedex/**  
 Exécuter la commande suivante : **python3 manage.py runserver**


## Voici la liste des routes disponibles avec les requêtes à faire :

- ```http://127.0.0.1:8000/api/moves/<int:move_id>/```  
    - Récupère le nom du mouvement en fonction de l'id entré dans l'url  
    - Requête **GET**  


- ```http://127.0.0.1:8000/api/pokemon/<int:pokemon_id>/```  
    - Récupère le nom du pokemon en fonction de l'id entré dans l'url  
    - Requête **GET**  


- ```http://127.0.0.1:8000/api/pokemon/<str:pokemon_name>/```  
    - Récupère le nom la hauteur, le poids et l'expérience de base en fonction du nom du pokemon entré dans l'url  
    - Requête **GET**  


- ```http://127.0.0.1:8000/api/pokemon/types/<str:pokemon_name>/```  
    - Récupère le le type en fonction du nom du pokemon entré dans l'url  
    - Requête **GET**  


- ```http://127.0.0.1:8000/api/items/<int:item_id>/```  
    - Récupère le nom de l'item en fonction de l'id entré dans l'url  
    - Requête **GET**  


- ```http://127.0.0.1:8000/api/connexion/```  
    - Permet à un utilisateur de se connecter et avoir un token pour un pseudo et mot de passe valide  
    - Requête **POST**  
###### Body JSON :  
```json  
{  
  "username" : "pseudo",  
  "password": "mdp"  
}  
```  

- ```http://127.0.0.1:8000/api/register/```  
    - Permet à un utilisateur de se créer un user avec un pokedex vide  
    - Requête **POST**  
###### Body JSON :  
```json  
{
  "username" : "pseudo",  
  "password": "mdp",  
  "role": "user"   // clé non obligatoire et à 'user' par défaut  
} 
```  

- ```http://127.0.0.1:8000/api/mesPokemons/```  
    - Permet à un utilisateur authentifié d'accéder à son pokedex (liste de pokemons)  
    - Requête **GET**  
    - Renseigner le Token dans Authentification/Bearer  


- ```http://127.0.0.1:8000/api/addPokemons/```  
    - Permet à un utilisateur authentifié d'ajouter un ou plusieurs pokemon(s) à son pokedex  
    - Requête **POST**  
    - Renseigner le Token dans Authentification/Bearer  
###### Body JSON :  
```json  
{
  "pokemons": ["pokemon_id", "pokemon_id", "..."]   // Les id sont des int  
} 
```  

- ```http://127.0.0.1:8000/api/remPokemons/```  
    - Permet à un utilisateur authentifié de supprimer un ou plusieurs pokemon(s) à son pokedex  
    - Requête **DELETE**  
    - Renseigner le Token dans Authentification/Bearer  
###### Body JSON :  
```json  
{
  "pokemons": ["pokemon_id", "pokemon_id", "..."]   // Les id sont des int  
} 
```  


- ```http://127.0.0.1:8000/api/role/```  
    - Permet à un admin authentifié de récupérer le rôle de tout le monde (users + admins)  
    - Requête **GET**  
    - Renseigner le Token dans Authentification/Bearer  (fonctionne uniquement avec les utilisateurs admin)


- ```http://127.0.0.1:8000/api/admin/users/```  
    - Permet à un admin authentifié de modifier le rôle à un user (admin -> user  ou  user -> admin)  
    - Requête **POST**  
    - Renseigner le Token dans Authentification/Bearer  (fonctionne uniquement avec les utilisateurs admin)
###### Body JSON :  
```json  
{
  "username" : "pseudo",
  "role": "nouveau_role"  
} 
```  