from django.db import models
from EntrepriseApp.models import Entreprise
import uuid
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.validators import MinValueValidator

class Expeditions(models.Model):
    reference = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        unique = True
    )
    poids_kg = models.DecimalField(
        max_digits=10,decimal_places=2,validators=[MinValueValidator(0.01)]
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
        on_delete=models.CASCADE,
        related_name='expeditions'
    )

    def clean(self):#comapring two attributes
         #
         #whenever we want to have a validator condition on somehtong out of the class we are working with like here we are making this validator on entreprise whhile we are on expeditions we use the clean function
        super().clean()
        if self.entreprise_id and self.entreprise.type_entreprise != "chargeur":
            raise ValidationError({'entreprise':'Une expedition ne peut etre que par une entreprise de type chargeur'})

    @classmethod    #we aer using this funciton s argument as a class because we arre trieving data so we need a class for them ot get filled in 
    #this generates a reference not a reference to each instance it only cares about the reference fo the last one the last reference the last person the last to create
    def _generate_reference(cls) : # this is to create a condition over the references we create they must be in a certain format that s what we are doing here
        anne = timezone.now().strftime('%y') # extraire annee of now

        dernier = cls.objects.filter(reference__startswith=f"EXP_{anne}").order_by('reference').last() # here we are extracting the objects that their attribute reference starts with EXP and a year and then we order them by reference ascending of -reference descanding and ge tthe last item 
        # dernier = cls.objects.filter(reference__startwith=f"EXP_{annee}").order_by('-reference').first()
        compteur = int(dernier.reference[-5:])+1 if dernier else 1 #here we get the last 5 caracters of the attribute reference from the objects we retirieved from the db if they exist if they don t let s just have 1 instead

        if compteur > 99999 : # here if the number is over 99999 we rause an exception
            raise ValidationError("Limite exceeded")
        return f""

    def save(self,*args,**kwargs):#this is for making sure that when we save when the user uses the submit button if there s no reference one must be createed and then we do a full clean wich would  make sure of that clean attribute we made earlier 
        if not self.reference :
            self.reference = self._generate_reference()
        self.full_clean()
        super().save(*args,**kwargs)