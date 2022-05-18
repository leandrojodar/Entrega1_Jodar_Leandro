from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
#from AppExcursiones import views
from AppExcursiones.models import Cliente, Destino, Hotel
from django.template import loader

# Create your views here.

# def "nombre"(request):
    #return HttpResponse(algo)

def cliente(request):
    cliente = cliente(nombre="Walter", apellido="Salinas", edad=38)
    cliente.save()
    doc_texto = f"Nombre: {cliente.nombre}, Apellido: {cliente.apellido}, Edad: {cliente.edad}"
    return HttpResponse(doc_texto)

def destino(request):
    destino = destino(pais="Belgica", excursion= "Bosque Antiguo", duracion= "2 dias", precio= "USD 100")
    destino.save()
    doc_texto_2 = f"País: {destino.pais}, Excursión: {destino.excursion}, Duración: {destino.duracion}, Precio: {destino.precio}"
    return HttpResponse(doc_texto_2)

def hotel(request):
    hotel = hotel(habitacion= "doble", camas= 1, banio= 1, wifi= "Si", numero= 320)
    hotel.save()
    doc_texto_3 = f"Habitación: {hotel.habitacion}, Cantidad de camas: {hotel.camas}, Cantidad de baños: {hotel.banios}, Wi-Fi: {hotel.wifi}, Número de habitación: {hotel.numero}"
    return HttpResponse(doc_texto_3)

def inicio(request):#No tengo una template de inicio creada
    return render(request, "AppExcursiones/inicio.html")

def clientes(request):
    return render(request, "AppExcursiones/clientes.html")

def destinos(request):
    return render(request, "AppExcursiones/destinos.html")

def hoteles(request):
    return render(request, "AppExcursiones/hoteles.html")

