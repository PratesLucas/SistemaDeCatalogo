from django.urls import path
from ata import views

urlpatterns = [
    path('atas/', views.atas_view, name='atas'),
    path('cadastro_ata/', views.cadastro_ata_view, name='cadastro_ata'),
]