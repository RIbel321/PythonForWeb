from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Vehicule
from . import forms


class VehiculeListView(ListView):
    model = Vehicule
    template_name = "vehicule/list.html"
    context_object_name = "vehicules"


class VehiculeDetailView(DetailView):
    model = Vehicule
    template_name = "vehicule/detailtest.html"
    context_object_name = "vehicule"


class VehiculeDeleteView(DeleteView):
    model = Vehicule
    template_name = "vehicule/vehiculedelete.html"
    context_object_name = "vehicule"
    success_url = reverse_lazy("vehicule:list_vehicule")


class VehiculeCreateView(CreateView):
    model = Vehicule
    template_name = 'vehicule/create.html'
    form_class = forms.VehiculeForm
    success_url = reverse_lazy("vehicule:list_vehicule")


class VehiculeUpdateView(UpdateView):
    model = Vehicule
    template_name = 'vehicule/create.html'
    form_class = forms.VehiculeForm
    success_url = reverse_lazy("vehicule:list_vehicule")
