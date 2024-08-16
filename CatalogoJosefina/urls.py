from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", include("pessoa.urls"), name='pessoa'),
    path("pessoa/", include("pessoa.urls"), name='pessoa'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path("accounts/", include ("accounts.urls")),
    path("accounts/", include ("django.contrib.auth.urls")),
    path("ata/", include ("ata.urls")),
    path('admin/', admin.site.urls),
]