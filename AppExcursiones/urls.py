from django.urls import path
from AppExcursiones import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('clientes', views.clientes, name="Clientes"),
    path('destinos', views.destinos, name="Destinos"),
    path('hoteles', views.hoteles, name="Hoteles"),
    #path('clienteFormulario/', views.clienteFormulario, name="ClienteFormulario"),
    #path('destinoFormulario/', views.destinoFormulario, name="DestinoFormulario"),
    #path('busquedaCamada/',  views.busquedaCamada, name="BusquedaCamada"),
    #path('buscar/', views.buscar),
   
]