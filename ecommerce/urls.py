from django.urls import path
from . import views

urlpatterns = [
   path('', views.paginaPrincipal, name="home"),
   path('contacto/', views.paginaContacto, name="contacto"),

   path('producto/<int:selectedValue>/', views.paginaContacto, name="contacto"),

   path('filtroInicio/<int:selectedValue>/', views.filtroInicio, name='filtroInicio'),
   path('filtroPrecio/<int:selectedPrize>/', views.filtroPrecio, name='filtroPrecio'),
   path('filtroProveedor/<int:selectedProveedor>/', views.filtroProveedor, name='filtroProveedor'),
   
   path('descProducto/<int:productId>/', views.descripcionProducto, name='descripcionProducto'),
   #path('', views.filtroInicio, name='filtroInicio'),
]