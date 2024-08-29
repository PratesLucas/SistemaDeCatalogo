from django.urls import path
from . import views

urlpatterns = [
    path('atas/', views.atas_view, name='atas'),
    path('ata/cadastro_ata/', views.cadastro_ata_view, name='cadastro_ata'),
    path('ata/edit_ata/<int:ata_id>/', views.edit_ata_view, name='edit_ata'),
    path('ata/remove_ata/<int:ata_id>/', views.remove_ata_view, name='remove_ata'),
    path('ata/ata/<int:ata_id>/arquivos/', views.ver_arquivos_ata, name='ver_arquivos_ata'),
    path('ata/ata/<int:ata_id>/upload/', views.upload_arquivo_pdf, name='upload_arquivo_pdf'),
    path('ata/arquivo/<int:arquivo_pdf_id>/editar/', views.editar_arquivo_pdf, name='editar_arquivo_pdf'),
    path('ata/arquivo/<int:arquivo_pdf_id>/excluir/', views.excluir_arquivo_pdf, name='excluir_arquivo_pdf'),
]
