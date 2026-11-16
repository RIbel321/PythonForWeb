from django.contrib import admin
from .models import Expedition
from OffresApp.models import Offres
from django.utils.html import format_html
import csv
from django.http import HttpResponse

# Register your models here.
admin.site.site_header = 'Transconnect - Administration'
admin.site.site_title = 'Transconnect'
admin.site.index_title="Gestion de la plateforme Transconnect"
class ExpeditionAdmin(admin.ModelAdmin):

    list_display=('reference',"entreprise",'statut','statut_badge')

    @admin.display(description='statut')
    def statut_badge(self,obj):
        couleurs={
            'livree':'green',
            'en_cours':'orange',
            'annulee':'red',
            'publiee':'blue',
        }
        couleur=couleurs.get(obj.statut,'gray')
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            couleur,
            obj.statut
        )
    
    def get_readonly_fields(self,request,obj=None):
        base = list(self.readonly_fields)
        if obj and obj.statut=='acceptee':
            return base + ['prix','delai_jours']
        return base

    

    list_filter=('statut',)
    search_fields=('reference','entreprise__matricule_fiscal')
    list_editable=('statut',)
    ordering=('created_at',)
    date_hierarchy='created_at' 
    list_per_page = 25
    fieldsets=(
        ('Informations generales', {
            'fields':('reference','entreprise')
        }),
        ('Informations sur le transport', {
            'fields':('poids_kg',)
        }),
        ('statut et dates',{
            'fields':('statut','created_at','updated_at'),
            'classes':('collapse',)
        })
        
        
        
        )
    readonly_fields=('reference',)
    autocomplete_fields=('entreprise',)



    class OffreInline(admin.TabularInline):#stackedinline
        model = Offres
        extra = 3

        readonly_fields= (
            'transporteur',
            'prix',
        )

        #fk_name=
        can_delete = True
        show_change_link=True

        def has_add_permission(self,request,obj=None):
            return False

    inlines = [OffreInline]

    @admin.action(description="Exporter la selection en csv")
    def exporter_offres_csv(modeladmin,request,queryset):
        response=HttpResponse(content_type='text/csv')
        response['Content-Disposition']='attachment;filename="offres.csv'
        writer=csv.writer(responsee)
        writer.writerow(['reference_expedition','transporteur','prix','statut'])
        for offre in queryset.select_related('expedition','transporteur'):  
            writer.writerow([
                offre.Expedition.reference,
                offre.transporteur.raison_sociale,
                offre.prix,
                offre.statut
            ])
        return response


    @admin.action(description="Colturer les expeditions selectionnees")
    def cloturer_expeditions(modeladmin,request,queryset):
        compteur=0
        for expedition in queryset:
            if expedition.statut=='en_cours':
                expedition.statut='livree'
                expedition.full_clean()
                expedition.save()
                compteur+=1
        modeladmin.message_user(request,"expeditions clotures")

    actions = [cloturer_expeditions,exporter_offres_csv]




    

    
admin.site.register(Expedition,ExpeditionAdmin)

