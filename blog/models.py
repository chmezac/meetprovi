from django.db import models
from django.contrib.auth.models import User

class Tipo_Lugar(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.nombre

class Lugar(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, default="")
    descripcion = models.TextField(max_length=5000, default="")
    comuna = models.CharField(max_length=200, default="")
    direccion = models.CharField(max_length=200, default="")
    latitud = models.DecimalField(max_digits=90, decimal_places=10, null=True, default=0, blank=True)
    longitud = models.DecimalField(max_digits=90, decimal_places=10, null=True, default=0, blank=True)
    estado = models.BooleanField(default=False)
    imagen = models.CharField(max_length=90000, default="http://blogs.uladech.edu.pe/pastillasgerenciales/wp-content/uploads/sites/18/2016/08/error-code-18.jpeg", blank=True)
    tipo_lugar = models.ForeignKey('Tipo_Lugar', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombre



class Persona(User):
    rut = models.CharField(max_length=9, default="")