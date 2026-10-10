from django.db import models
from ExpeditionsApp.models import Expeditions
from VehiculeApp.models import Vehicule
from EntrepriseApp.models import Entreprise
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models,transaction



class Offre(models.Model):
    prix = models.DecimalField(
        max_digits = 10,
        decimal_places = 2,
        validators = [MinValueValidator(0.01,"Le prix doit etre superieur a 0")],        
    )

    delai_jours = models.PositiveIntegerField(validators=[MinValueValidator(1)])

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

    def clean(self):
        if (self.transporteur_id and self.type_transporteur != 'transporteur'):
            raise ValidationError({'Entreprise':'doit etre de type transporteur'})
        if (self.transporteur_id and self.vehicule_id):
            if self.vehicule.entreprise_id != self.transporteur_id :
                raise ValidationError({'Vehicule':'Cette vehicule doit etre avec le meme transporteur que l offre'})
        if (self.expedition and self.expedition_id.statut != 'publiee'):
            raise ValidationError({'Expedition':'on ne peut pas cree un offre avec une expedition qui n est pas publiee'})
        if (self.pk and self.expedition_id and self.transporteur_id and self.statut=='proposee'):
            offres_existantes=Offre.objects.filter(expedition_id=self.expedition_id,transporteur_id=self.transporteur_id
            ,statut='proposee')
            if self.pk:
                offres_existantes=offres_existantes.exclude(pk=self.pk)
            if offres_existantes.exists():
                raise ValidationError('Cette entreprise a deja une offre active pour cette expedition')
        if(self.vehicule and not self.vehicule.disponible):
            raise ValidationError('Cette vehicule n est pas disponible')
        if (self.vehicule_id and self.expedition_id):
            poids=self.expedition.poids_kg
            capacites_max = {
            'camionnette': 1500,
            'fourgon': 3500,
            'camion_porteur': 19000,
            'semi_remorque': 26000,
            }
            type_vehicule=self.vehicule.type_vehicule
            capacites_max=capacites_max[type_vehicule]
            if poids > capacite_max:
                raise ValidationError({
                    'vehicule': (
                        f"Le véhicule de type {type_vehicule} "
                        f"ne peut pas transporter une expédition de {poids} kg."
                    )
                })


    def save(self, *args, **kwargs):
        with transaction.atomic():
            anicent_statut=None
            if self.pk :
                ancienne_offre=Offre.objects.get(pk=self.pk)
                anicent_statut=ancienne_offre.statut
                self.expedition.statut='attribuee'
                self.expedition.save()
                Offre.objects.filter(expedition_id=self.expedition_id,statut='proposee').exclude(pk=self.pk).update(statut='refusee')
        sef.full_clean()
        super().save(*args, **kwargs)