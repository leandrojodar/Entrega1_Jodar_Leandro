from unittest.util import _MAX_LENGTH
from django.db import models
#from django.forms import CharField, IntegerField
#from AppExcursiones.models import Cliente, Destino, Hotel

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()

class Destino(models.Model):
    pais=models.CharField(max_length=100)
    excursion=models.CharField(max_length=100)
    duracion=models.CharField(max_length=30)
    precio=models.CharField(max_length=30)

class Hotel(models.Model):
    habitacion=models.CharField(max_length=20)
    camas=models.IntegerField()
    banio=models.IntegerField()
    wifi=models.CharField(max_length=5)
    numero=models.IntegerField()

#cliente = Cliente(nombre = "Walter", apellido = "Salinas", edad = 38)    