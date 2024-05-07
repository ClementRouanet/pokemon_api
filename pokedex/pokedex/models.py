from django.db import models
from django.contrib.auth.hashers import make_password, check_password



# Classe des mouvements 
class Move(models.Model) :
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=100)
    generation_id = models.IntegerField()
    type_id = models.IntegerField()
    power = models.IntegerField()
    pp = models.IntegerField()
    priority = models.IntegerField()
    target_id = models.IntegerField()
    damage_class_id = models.IntegerField()
    effect_id = models.IntegerField()
    effect_chance = models.IntegerField()
    contest_type_id = models.IntegerField()
    contest_effect_id = models.IntegerField()
    super_contest_effect_id = models.IntegerField()

    class Meta :
        db_table = 'moves'



# Classe des pokemons 
class Pokemon(models.Model) :
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=100)
    species_id = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField()
    order = models.IntegerField()
    is_default = models.IntegerField()


    class Meta :
        db_table = 'pokemon'



# Classe des types de pokemons 
class Pokemon_Types(models.Model) :
    pokemon_id = models.IntegerField(primary_key=True)
    type_id = models.IntegerField()
    slot = models.IntegerField()


    class Meta :
        db_table = 'pokemon_types'



# Classe des types
class Types(models.Model) :
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=100)
    generation_id = models.IntegerField()
    damage_class_id = models.IntegerField()


    class Meta :
        db_table = 'types'



# Classe des items
class Item(models.Model) :
    identifier = models.CharField(max_length=100)

    class Meta :
        db_table = 'items'



# Classe des users
class User(models.Model) :
    id = models.AutoField(primary_key=True)
    pseudo = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)


    # Fonction pour créer un nouvel utilisateur
    def create_user(self, pseudo, password, role='user') :
        password_hash = make_password(password)

        self.pseudo = pseudo
        self.password = password_hash
        self.role = role

        self.save()
    

    # Fonction qui vérifie l'exactitude du mot de passe lors de l'authentification
    def check_password(self, password) :
        return check_password(password, self.password)
    

    # Fonction qui renvoie vrai si l'utilisateur est un admin et faux sinon
    def is_admin(self) :
        return self.role == 'admin'


    class Meta :
        db_table = 'user'



# Classe des sacs (pokedex)
class Bag (models.Model) :
    user_id = models.IntegerField(primary_key=True)
    pokemon_id = models.IntegerField()


    class Meta :
        db_table = 'bag'