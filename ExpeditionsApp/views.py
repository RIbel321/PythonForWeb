from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Expedition

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.views.generic import UpdateView

from django.urls import reverse_lazy
from . import forms

# Create your views here.

class ExpeditionListView(ListView):
    model = Expedition
    template_name = "expeditions/list.html"
    context_object_name = "expeditions"

class ExpeditionDetailView(DetailView):
    model = Expedition
    template_name = "expeditions/detailtest.html"
    context_object_name = "expedition"

class ExpeditionDeleteView(DeleteView):
    model = Expedition
    template_name = "expeditions/expeditiondelete.html"
    context_object_name = "expedition"
    success_url = reverse_lazy("expedition:list_exped")

class ExpeditionCreateView(CreateView):
    model = Expedition
    template_name = 'expeditions/create.html'
    form_class = forms.ExpeditionForm
    success_url = reverse_lazy("expedition:list_exped")
    
class ExpeditionUpdateView(UpdateView):
    model = Expedition
    template_name = 'expeditions/create.html'
    form_class = forms.ExpeditionForm
    success_url = reverse_lazy("expedition:list_exped")


def list_expedition(request):
    expeditions = Expedition.objects.all()

    return render(request, 'expeditions/list.html', {    
        'expeditions': expeditions
    })


def detail(request, reference):
    expedition = get_object_or_404(Expedition, reference=reference)
    return render(request, 'expeditions/detail.html', {
        'expedition': expedition
    })


def supprimer(request, reference):
    if request.method == "POST":
        expedition = get_object_or_404(Expedition, reference=reference)
        expedition.delete()
        return redirect('expedition:All_exped')
    return HttpResponseBadRequest("Invalid request")
