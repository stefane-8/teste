from django.urls import path
from .views import login_view, register_view
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", login_view, name="login"),
    path("perfil/", views.meu_perfil, name='meu_perfil'),
    path("register/", register_view, name="register"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("diretoria/", views.diretoria_dashboard, name='admin_dashboard'),
    path("associado/", views.associado_dashboard, name='associado_dashboard'),
    path("coletivo/", views.coletivo_dashboard, name='coletivo_dashboard'),
]
