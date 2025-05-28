from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   
    path('menu/', views.menu_principal, name='menu'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('edicionMascota/<int:id>/', views.edicionMascota, name='edicionMascota'),
    path('editarMascota/', views.editarMascota, name='editarMascota'),
    path('eliminarMascota/<int:id>/', views.eliminarMascota, name='eliminarMascota'),
    path('mascotas/', views.gestion_mascota, name='gestion_mascota'),
    path('registrarMascota/', views.registrarMascota, name='registrarMascota'),

    path('duenos/', views.gestion_dueno, name='gestion_dueno'),
    path('registrarDueno/', views.registrarDueno, name='registrarDueno'),
    path('edicionDueno/<str:rut>/', views.edicionDueno, name='edicionDueno'),
    path('editarDueno/', views.editarDueno, name='editarDueno'),
    path('eliminarDueno/<str:rut>/', views.eliminarDueno, name='eliminarDueno'),
    path('detalleDueno/<str:rut>/', views.detalle_dueno, name='detalle_dueno'),


  
    path('especie/', views.gestion_especie, name='gestion_especie'),
    path('registrarEspecie/', views.registrarEspecie, name='registrarEspecie'),
    path('edicionEspecie/<int:id>/', views.edicionEspecie, name='edicionEspecie'),
    path('editarEspecie/', views.editarEspecie, name='editarEspecie'),
    path('eliminarEspecie/<int:id>/', views.eliminarEspecie, name='eliminarEspecie'),

]
