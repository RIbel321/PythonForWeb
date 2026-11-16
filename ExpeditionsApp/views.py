from django.shortcuts import render
from django.http import HttpResponse
from .models import Expedition
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
# Create your views here.


def list_expedition(request):
    expeditions=Expedition.objects.all()

    return render(request,'expeditions/list.html',{    
        'expeditions':expeditions
    })


def detail(request,reference):
    expedition=get_object_or_404(Expedition,reference=reference)
    return render(request,'expeditions/detail.html',{
        'expedition':expedition
    }
    )


def supprimer(request,reference):
    if request.method=="POST":
        expedition=get_object_or_404(Expedition,reference=reference)
        expedition.delete()
        return redirect('expedition:All_exped')
    return HttpResponseBadRequest("Invalid request")

