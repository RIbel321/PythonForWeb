from django.db import models

from VehiculeApp.models import Vehicule
from EntrepriseApp.models import Entreprise
from ExpeditionsApp.models import Expedition
from django.core.exceptions import ValidationError
from django.db import transaction
# Create your models here.
class Offres(models.Model):
    prix=models.DecimalField(max_digits=20,decimal_places=2)
    delai_jours=models.PositiveIntegerField()
    statut=models.CharField(choices=[
        ('proposee','Proposee'),
        ('acceptee','Acceptee'),
        ('proposee','Proposee'),
        ('refusee','Reufusee'),
        ('retiree','retiree')
    ],default='proposee')
    date_proposition=models.DateField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    expedition=models.ForeignKey(
        Expedition,on_delete=models.CASCADE
    )
    transporteur=models.ForeignKey(
        Entreprise,on_delete=models.CASCADE
    )
    vehicule=models.ForeignKey(
        Vehicule,on_delete=models.CASCADE   
    )

    def clean(self):
        super().clean()
        #if(self.transporteur_id and self.transporteur.type_entreprise!='transporteur'):
        #    raise ValidationError("L entreprise de cette offre doit etre de type transporteur")
        if(self.vehicule_id and self.transporteur_id and self.vehicule.Entreprise!=self.transporteur):
            raise ValidationError("Cette Vehicule doit appartenir au meme transporteur ")
        if (self.expedition_id and self.expedition.statut!='publiee'):
            raise ValidationError("Cette offre doit avoir une statut publiee")

        if (self.expedition_id and self.transporteur_id and self.statut=='proposee'):
            offresproposee=Offres.objects.filter(statut='proposee')
            offressimilaire=offresproposee.filter(expedition_id=self.expedition_id , transporteur_id=self.transporteur_id).exclude(pk=self.pk)
            if offressimilaire:
                raise ValidationError("on ne peut pas avoir deux offres au statut proposee actives simultanement sur la meme expedition")

        if (self.vehicule_id and not self.vehicule.disponible):
            raise ValidationError("Cette Voiture n est pas disponible")
        if (self.vehicule_id and self.vehicule.type_vehicule=='camionette' and self.expedition.poids_kg/1000>1.5):
            raise ValidationError("incompatibilite avec la capacite en T")
        if (self.vehicule_id and self.vehicule.type_vehicule=='camion_porteur' and (self.expedition.poids_kg/1000>19 or self.expedition.poids_kg/1000<3.5)):
            raise ValidationError("incompatibilite avec la capacite en T")
        if (self.vehicule_id and self.vehicule.type_vehicule=='semi_remorque' and (self.expedition.poids_kg/1000<19 or self.expedition.poids_kg/1000>26)):
            raise ValidationError("incompatibilite avec la capacite en T")
        if (self.vehicule_id and self.vehicule.type_vehicule=='fourgon' and self.expedition.poids_kg/1000>3.5):
            raise ValidationError("incompatibilite avec la capacite en T")

    def accepter(self):
        with transaction.atomic():
            if (self.statut=='proposee'):
                self.statut="acceptee"
                self.save()
                self.expedition.statut='attribuee'
                self.expedition.save()
                others=Offres.objects.filter(expedition_id=self.expedition_id,statut='proposee').exclude(pk=self.pk)
                others.update(statut='refusee')
    
    def save(self,*args,**kwargs):
        with transaction.atomic():
            if self.pk :
                ancienne_offres=Offres.objects.get(pk=self.pk)
                ancienne_statut=ancienne_offres.statut
                if (self.statut=='acceptee' and ancienne_statut=='proposee'):
                    self.expedition.statut='attribuee'
                    self.expedition.save()
                    others=Offres.objects.filter(expedition_id=self.expedition_id,statut='proposee').exclude(pk=self.pk)
                    others.update(statut='refusee')
            self.full_clean()
            super().save(*args,**kwargs)
