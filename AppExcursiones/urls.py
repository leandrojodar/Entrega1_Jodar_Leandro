from django.urls import path
from AppExcursiones import views

urlpatterns = [
   
    #path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('cliente', views.cliente, name="Clientes"),
    path('destino', views.destino, name="Destinos"),
    path('hotel', views.hotel, name="Hoteles"),
    #path('clienteFormulario', views.clienteFormulario, name="ClienteFormulario"),
    #path('destinoFormulario', views.destinoFormulario, name="DestinoFormulario"),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    #path('buscar/', views.buscar),
   
]