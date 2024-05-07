#              API et Web Services   -   Projet Pokedex  
  

Réalisé par HOUKMI Salaheddine & ROUANET Clément  
M2 data Engineering & AI  -  EFREI Paris


## Lancement du programme :
 Se placer dans le chemin : **/pokemon_api/pokedex/**  
 Exécuter la commande suivante : **python3 manage.py runserver**


## Voici la liste des routes disponibles avec les requêtes à faire :

- ```http://127.0.0.1:8000/api/moves/<int:move_id>/```  
Récupère le nom du mouvement en fonction de l'id entré dans l'url  


- ```http://127.0.0.1:8000/api/pokemon/<int:pokemon_id>/```  
Récupère le nom du pokemon en fonction de l'id entré dans l'url  


- ```http://127.0.0.1:8000/api/pokemon/<str:pokemon_name>/```  
Récupère le nom la hauteur, le poids et l'expérience de base en fonction du nom du pokemon entré dans l'url  


- ```http://127.0.0.1:8000/api/pokemon/types/<str:pokemon_name>/```  
Récupère le le type en fonction du nom du pokemon entré dans l'url  


- ```http://127.0.0.1:8000/```


- ```http://127.0.0.1:8000/```