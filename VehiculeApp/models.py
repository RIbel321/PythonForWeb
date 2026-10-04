from django.db import models
from EntrepriseApp.models import Entreprise


class Vehicule(models.Model):
    capacite_kg= models.PositiveIntegerField()


    immatriculation = models.CharField(
        max_length=100,
        unique = True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


    entreprise= models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE
    )