from django.urls import path
from . import views

urlpatterns = [
   path('', views.paginaPrincipal, name="home"),
   path('contacto/', views.paginaContacto, name="contacto"),
   
]