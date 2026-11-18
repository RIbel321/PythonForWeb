from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Offres
from . import forms


class OffresListView(ListView):
    model = Offres
    template_name = "offres/list.html"
    context_object_name = "offres"


class OffresDetailView(DetailView):
    model = Offres
    template_name = "offres/detailtest.html"
    context_object_name = "offre"


class OffresDeleteView(DeleteView):
    model = Offres
    template_name = "offres/offresdelete.html"
    context_object_name = "offre"
    success_url = reverse_lazy("offres:list_offres")


class OffresCreateView(CreateView):
    model = Offres
    template_name = 'offres/create.html'
    form_class = forms.OffresForm
    success_url = reverse_lazy("offres:list_offres")


class OffresUpdateView(UpdateView):
    model = Offres
    template_name = 'offres/create.html'
    form_class = forms.OffresForm
    success_url = reverse_lazy("offres:list_offres")


# Aliases (singular)
OffreListView = OffresListView
OffreDetailView = OffresDetailView
OffreDeleteView = OffresDeleteView
OffreCreateView = OffresCreateView
OffreUpdateView = OffresUpdateView
