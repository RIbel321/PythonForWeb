from django.shortcuts import render
from django.http import HttpResponse
from .models import Entreprise
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.views.generic import UpdateView


from django.urls import reverse_lazy
from . import forms 





class EntrepriseListView(ListView):
    model=Entreprise
    template_name="entreprise/list.html"
    context_object_name="entrepriser"
    
class EntrepriseDetailView(DetailView):
    model=Entreprise
    template_name="entreprise/detailtest.html"
    context_object_name="entreprise"

class EntrepriseDeleteView(DeleteView):
    model = Entreprise
    template_name="entreprise/entreprisedelete.html"
    context_object_name="entreprise"
    success_url=reverse_lazy("entreprise:list_ent")

class EntrepriseCreateView(CreateView):
    model = Entreprise
    template_name='entreprise/create.html'
    form_class=forms.EntrepriseForm
    success_url=reverse_lazy("entreprise:list_ent")
    
class EntrepriseUpdateView(UpdateView):
    model = Entreprise
    template_name = 'entreprise/create.html'
    form_class = forms.EntrepriseForm
    success_url = reverse_lazy("entreprise:list_ent")




# Create your views here.
def home(request):
    #return HttpResponse("Welcome to transconnect")
    #HttpResponseNotFound()
    #companies = ['FedEX','Amazon','Netflix']
    companies = []
    return render(request,'entreprise/test.html',{
        'name':'Ribel',
        'city':'Tunis',
        'age':'20',
        'Companies':companies,
        'is_admin':False,
        'role':'transporteur'
    })

def detail_entreprise(request):#,reference add it in the arguments if you are 
    #entrepriser=get_object_or_404(Entreprise,matricule_fiscal=reference)
    spec=Entreprise.objects.filter(type_entreprise='chargeur').select_related('utilisateur').order_by('-created_at')
    return render(request,'entreprise/detail.html',{
        'entrepriser':spec,

    })#'reference':reference, if i want it returned as well to enter it into the html


def liste_entreprise(request):
    entreprises=Entreprise.objects.all()

    return render(request,'entreprise/list.html',{
        'entreprises':entreprises
    })



def liste_entreprised(request):
    entreprises=Entreprise.objects.all()
    #entreprises=Entreprise.objects.filter(type_entreprise='chargeur').select_related('utilisateur').order_by('-created_at') for filtering

    return render(request,'entreprise/detail.html',{    
        'entreprises':entreprises
    })


#def detail(request, reference):
#    try:
#        entreprise = Entreprise.objects.get(matricule_fiscal=reference)
#    except Entreprise.DoesNotExist:
#        return HttpResponseNotFound("Entreprise not found")

#    return HttpResponse(entreprise.matricule_fiscal) same as doing it with oobject_or404

#def liste_entreprise(request):
#    return redirect('entreprise:home') # this is render it changer where a path takes you here it changed how the original path of the funciton liste entreprise works and took m eto enretprise:home path it s used often in delete after deletin it automatically takes me ot another page for example


def detail2(request,reference):
    entreprise=get_object_or_404(Entreprise,matricule_fiscal=reference)
    return render(request,'entreprise/detail2.html',{
        'entreprise':entreprise
    }
    )
#to show the details of each one we simply use a reference that reads the reference and pass it as an arg to show it twith the detail funciton in another detail page to create this we need a href link htat passes it down so that link need to be filled with the reference he is going to send and for that in the href we nned to provide it with the loop each loop provides one link by hte other function previous one that extracts all of them from the database and then they loop inside the html file and each time a reference from the database is given to one href link

def supprimer(request,reference):
    if request.method=="POST":
        entreprise=get_object_or_404(Entreprise,matricule_fiscal=reference)
        entreprise.delete()
        return redirect('entreprise:All')
    return HttpResponseBadRequest("Invalid request")


