from django.urls import path
from . import views

urlpatterns = [
   path('', views.paginaPrincipal, name="home"),
   path('showmore/',  views.showmoreView, name='show_more'),
   path('contacto/', views.paginaContacto, name="contacto"),

   path('update/<int:product_id>/' , views.update_product, name='update_product'),
   path('create/', views.create_product, name='create_product'),
   path('createUser/', views.create_user, name='create_user'),
   
   path('editUser/<int:user_id>/', views.edit_user, name='edit_user'),

   path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
   path('deleteUser/<int:user_id>/', views.delete_user, name='delete_user'),
   path('producto/<int:selectedValue>/', views.paginaContacto, name="contacto"),
   

   path('filtroInicio/<int:selectedValue>/', views.filtroInicio, name='filtroInicio'),
   path('filtroPrecio/<int:selectedPrize>/', views.filtroPrecio, name='filtroPrecio'),
   path('filtroProveedor/<int:selectedProveedor>/', views.filtroProveedor, name='filtroProveedor'),
   
   path('descProducto/<int:productId>/', views.descripcionProducto, name='descripcionProducto'),
   #path('', views.filtroInicio, name='filtroInicio'),

   path('login/', views.iniciarSesion, name="login"),
   path('registro/', views.registrarse, name="registro"),
   path('logout/', views.logoutUser, name="logout"),
]