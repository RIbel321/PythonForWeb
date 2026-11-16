from django.urls import path
from . import views

app_name = 'expedition'

urlpatterns = [
    path('list/',views.list_expedition, name='All_exped'),
    path('delete/<path:reference>/',views.supprimer,name='supprimer_exped'),
    path('<path:reference>/',views.detail,name='detail_exped'),
]
