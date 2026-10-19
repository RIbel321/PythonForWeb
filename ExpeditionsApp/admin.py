from django.contrib import admin
from .models import Expeditions
# Register your models here.
class ExpeditionAdmin(admin.ModelAdmin):
    list_display = ('reference','poids_kg')
    #    list_display = ('reference','ville depart','ville arrive','poid')
    search_fields=(
        "reference",
        "entreprise__raison_sociales"
    )
admin.site.register(Expeditions,ExpeditionAdmin)
