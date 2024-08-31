from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="read"),
    path("<int:pessoa_id>/", views.details, name="details"),
    path("add/", views.add, name="create"),
    path("edit/<int:pessoa_id>/", views.edit, name="refresh"),
    path("remove/<int:pessoa_id>/", views.remove, name="delete"),
]
