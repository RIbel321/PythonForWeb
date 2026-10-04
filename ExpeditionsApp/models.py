from django.db import models
from EntrepriseApp.models import Entreprise
import uuid


class Expeditions(models.Model):
    reference = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        unique = True,
        default = uuid.uuid4
    )
    poids_kg = models.DecimalField(
        max_digits=10,decimal_places=2
    )
    statut= models.CharField(
        max_length=100,
        choices=[
            ('publiee', 'Publiee'),
            ('attribuee', 'Attribuee'),
            ('en_cours', 'En cours'),
            ('annulee', 'Annulee'),
            ('livree', 'Livree'),
        ],
        default='publiee'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


    entreprise = models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE
    )