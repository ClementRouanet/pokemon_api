from django.db import models

class Move(models.Model):
    identifier  = models.CharField(max_length=100)
    # Autres champs pour le modèle Move

    class Meta:
        db_table = 'moves'

