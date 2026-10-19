from django.contrib import admin
from .models import Expeditions
# Register your models here.
class EnRetardFilter(admin.SimpleListFilter):
    title = 'en retard'
    parameter_name = 'en_retard'
    def lookups(self,request,model_admin):
        return [('oui','Oui'),('non','Non')]
    def queryset(self,request,queryset):
        aujourd_hui = timezone.now().date()
        if self.value() == "oui" :
            return queryset.filter(statut="publiee",date_souhaite__lt=aujourd_hui)
        if self.value() == "non":
            return queryset.exclude(statut="publiee",date_souhaitee__lt=aujourd_hui)
        return queryset

class ExpeditionAdmin(admin.ModelAdmin):
    list_display = ('reference','poids_kg')
    #    list_display = ('reference','ville depart','ville arrive','poid')
    search_fields=(
        "reference",
        "entreprise__raison_sociale"
    )
    readonly_fields=(
        "created_at","updated_at"
    )
   
    fieldsets = (
        (
            "Expedition",
            {
                "fields": (
                    "reference",
                    "entreprise",
                ),
            },
        ),
        (
            "Itineraire et poids",
            {
                "fields": (
                    "poids_kg",
                ),
            },
        ),
        (
            "Statut et horodatage",
            {
                "fields": (
                    "statut",
                    "created_at",
                    "updated_at",
                ),
                "classes": ("collapse",),
            },
        ),
    )

#fieldsets=(
#       ("Expedition" ,
#            {"fields" : (
#                "reference",
#                "entreprise"
#                #,"description"
#            )
#            }
#        ),
#        ("Itineraire et poids",
#        {"fields" : ( "poids_kg",
#        #"date_souhaite", "ville_depart","vilee_arrivee",
#        )},
#        "Statut et horodatage"),
#        (
#        {"fields" :("statut","created_at","updated_at"),
#        "classes":("collapse",),},
#    ),
#    )
admin.site.register(Expeditions,ExpeditionAdmin)
