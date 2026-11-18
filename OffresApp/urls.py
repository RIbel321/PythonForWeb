from django.urls import path
from . import views

app_name = 'offres'

urlpatterns = [
    path('list/', views.OffresListView.as_view(), name='list_offres'),
    path('detail/<int:pk>/', views.OffresDetailView.as_view(), name='detail_offres'),
    path('offre_delete/<int:pk>/', views.OffresDeleteView.as_view(), name='offre_delete'),
    path('offres_delete/<int:pk>/', views.OffresDeleteView.as_view(), name='offres_delete'),
    path('offre_create/', views.OffresCreateView.as_view(), name='offre_create'),
    path('offres_create/', views.OffresCreateView.as_view(), name='offres_create'),
    path('offre_update/<int:pk>/', views.OffresUpdateView.as_view(), name='offre_update'),
    path('offres_update/<int:pk>/', views.OffresUpdateView.as_view(), name='offres_update'),
]

