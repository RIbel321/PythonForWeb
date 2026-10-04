class Offre(models.Model):
	prix = models.CharField(max_length=10)
	delai_jours = models.IntegerField()
	statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='proposee')
	date_proposition = models.DateField(auto_now=True)
	expedition = models.ForeignKey(Expedition, on_delete=models.CASCADE)
	transporteur = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
	vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, null=True)
	
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		
Correction :

class Offre(models.Model):
	prix = models.DecimalField(max_digits=100,decimal_places=100)
	delai_jours = models.PositiveIntegerField()
	statut = models.CharField(max_length=20, choices=[
            ('proposee', 'Proposee'),
            ('acceptee', 'Acceptee'),
            ('refusee', 'Refusee'),
            ('retiree', 'Retiree'),
        ], default='proposee')
	date_proposition = models.DateField(auto_now_add=True)
	
	expedition = models.ForeignKey(Expedition, on_delete=models.CASCADE)
	
	transporteur = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
	
	vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
	
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		
	
##Entree Oct4 19:34
	Outil : chatgpt
	Prompt : When i make migrations here it keeps telling me that there s a problem with spaces with the lign created at i didn t understand the error and if you mind explaining why when i did this models without the def save it told me that i cant create a database with a non nullable something i forgot what it said exactly , it was talking about the vehicules and the offres tables as it couldn t add it why did it work now ? 
	class Offre(models.Model):
	prix = models.DecimalField(max_digits=100,decimal_places=100)
	delai_jours = models.PositiveIntegerField()
	statut = models.CharField(max_length=20, choices=[
            ('proposee', 'Proposee'),
            ('acceptee', 'Acceptee'),
            ('refusee', 'Refusee'),
            ('retiree', 'Retiree'),
        ], default='proposee')
	date_proposition = models.DateField(auto_now_add=True)
	
	expedition = models.ForeignKey(Expedition, on_delete=models.CASCADE)
	
	transporteur = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
	
	vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
	
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		
	
	Sortie obtenue (resume) + avec la correction: it was not because of hte save method it was because i deleted the database and recreated it again so django could create the new non null columns without any problems and for the save method it simply calls for the django s normal save method it simply inherits it , and the first problem was because of identation and spaces with the save method apparantly the code had mixed identations with tabs and spaces 


