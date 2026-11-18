from django.urls import path
from . import views

app_name = 'vehicule'

urlpatterns = [
    path('list/', views.VehiculeListView.as_view(), name='list_vehicule'),
    path('detail/<int:pk>/', views.VehiculeDetailView.as_view(), name='detail_vehicule'),
    path('vehicule_delete/<int:pk>/', views.VehiculeDeleteView.as_view(), name='vehicule_delete'),
    path('vehicule_create/', views.VehiculeCreateView.as_view(), name='vehicule_create'),
    path('vehicule_update/<int:pk>/', views.VehiculeUpdateView.as_view(), name='vehicule_update'),
]

