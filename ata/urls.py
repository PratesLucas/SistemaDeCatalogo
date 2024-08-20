from django.urls import path
from ata import views

urlpatterns = [
    path('atas/', views.atas_view, name='atas'),
    path('cadastro_ata/', views.cadastro_ata_view, name='cadastro_ata'),
    path('edit_ata/<int:ata_id>/', views.edit_ata_view, name='edit_ata'),
    path('remove_ata/<int:ata_id>/', views.remove_ata_view, name='remove_ata'),
]