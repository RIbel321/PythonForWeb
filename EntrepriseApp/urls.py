from django.urls import path
from . import views


app_name = 'entreprise'

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.EntrepriseListView.as_view(),name='list_ent'),
    path('detail/<int:pk>/',views.EntrepriseDetailView.as_view(),name='detail_ent'),
    path('entreprise_delete/<int:pk>/',views.EntrepriseDeleteView.as_view(),name='entreprise_delete'),
    path('entreprise_create/',views.EntrepriseCreateView.as_view(),name='entreprise_create'),
    path('entreprise_update/<int:pk>/', views.EntrepriseUpdateView.as_view(), name='entreprise_update'),





    path('listV/', views.liste_entreprise, name='liste_entreprise'),
    path('entreprise_filtre/', views.detail_entreprise, name='filtre'),
    path('entreprise/detail/', views.liste_entreprised, name='All'),
    path('delete/<path:reference>/',views.supprimer,name='supprimer'),
    path('<path:reference>/',views.detail2,name='detail2'),


]

#repath something like path it only reads paths as regex for example re_path(r'ĥello/(?P<name>[a-z]+)/$',views.hello,name='hello')

#when putting a path that reads an arng and a normal path for example 
#str:reference
#list/
#in this order if i enter list/ django will read it as an arg and enter it though it s a link a vlaid link for that i must order by 
#list/
#then str:reference


#in the html files the filter | can be upper lower titele to capitalize eaech word capfirst capitalize the first characters default dispay a fallback value or trauncatewords:5 to limit dispayed text to 5 words and length calculates the number of characters
#with a path arg it can interpret /delete/something as an arg because path is greedy so one having only path in it should be in last