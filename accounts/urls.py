from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.createuser, name='adduser'),
    path('', views.listusers, name='list_users'),
    path('edit/<int:id>/', views.edituser, name='edit_user'),
    path('delete/<int:id>/', views.deleteuser, name='delete_user'),
]