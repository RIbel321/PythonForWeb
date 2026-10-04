from django.db import models
from ExpeditionsApp.models import Expeditions
from VehiculeApp.models import Vehicule
from EntrepriseApp.models import Entreprise


class Offre(models.Model):
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    delai_jours = models.PositiveIntegerField()

    statut = models.CharField(
        max_length=20,
        choices=[
            ('proposee', 'Proposee'),
            ('acceptee', 'Acceptee'),
            ('refusee', 'Refusee'),
            ('retiree', 'Retiree'),
        ],
        default='proposee'
    )

    date_proposition = models.DateField(auto_now_add=True)

    expedition = models.ForeignKey(
        Expeditions,
        on_delete=models.CASCADE
    )

    transporteur = models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE
    )

    vehicule = models.ForeignKey(
        Vehicule,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)