from django.db import models

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



class Pokemon_Types(models.Model) :
    pokemon_id = models.IntegerField()
    type_id = models.IntegerField()
    slot = models.IntegerField()


    class Meta :
        db_table = 'pokemon_types'



class Types(models.Model) :
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=100)
    generation_id = models.IntegerField()
    damage_class_id = models.IntegerField()


    class Meta :
        db_table = 'types'