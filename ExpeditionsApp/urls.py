from django.urls import path
from . import views

app_name = 'expedition'

urlpatterns = [
    path('list/', views.ExpeditionListView.as_view(), name='list_exped'),
    path('detail/<int:pk>/', views.ExpeditionDetailView.as_view(), name='detail_exped'),
    path('expedition_delete/<int:pk>/', views.ExpeditionDeleteView.as_view(), name='expedition_delete'),
    path('expeditions_delete/<int:pk>/', views.ExpeditionDeleteView.as_view(), name='expeditions_delete'),
    path('expedition_create/', views.ExpeditionCreateView.as_view(), name='expedition_create'),
    path('expedition_update/<int:pk>/', views.ExpeditionUpdateView.as_view(), name='expedition_update'),
    path('expeditions_update/<int:pk>/', views.ExpeditionUpdateView.as_view(), name='expeditions_update'),

    path('listV/', views.list_expedition, name='All_exped'),
    path('deleteV/<path:reference>/', views.supprimer, name='supprimer_exped'),
    path('<path:reference>/VAZ/', views.detail, name='detail_exped_ref'),
]
