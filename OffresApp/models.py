from django.db import models
from ExpeditionsApp.models import Expeditions


class Offres(models.Model):
    delai_jours = models.PositiveIntegerField()
    prix = models.DecimalField(
        max_digits=100,decimal_places=100
    )

    statut= models.CharField(
        max_length=100,
        choices=[
            ('proposee', 'Proposee'),
            ('acceptee', 'Acceptee'),
            ('refusee', 'Refusee'),
            ('retiree', 'Retiree'),
        ]
        ,default='proposee'
    )
    Date_proposition = models.DateTimeField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


    expedition = models.ForeignKey(
        Expeditions,
        on_delete=models.CASCADE
    )