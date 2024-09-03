from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="read"),
    path("<int:pessoa_id>/", views.details, name="details"),
    path("add/", views.add, name="create"),
    path("endereco/add/<int:id>/", views.add_endereco, name="create_endereco"),
    path("endereco/edit/<int:id>/", views.edit_endereco, name="edit_endereco"),
    path("endereco/remove/<int:id>/", views.remove_endereco, name="delete_endereco"),
    path("edit/<int:pessoa_id>/", views.edit, name="refresh"),
    path("remove/<int:pessoa_id>/", views.remove, name="delete"),
    path("listagem/<str:tipo>/", views.index, name="read"),
]