from django.db import models

# Create your models here.
class Producto(models.Model):
    descripcion = models.CharField(max_length=60)
    presentacion = models.CharField(max_length=50)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre
        
class Sucursal(models.Model):
    nombre = models.CharField(max_length=100, default="Sucursal Principal")
    direccion = models.TextField(default="Por definir")
    ciudad = models.CharField(max_length=50, default="Ciudad desconocida")
    telefono = models.CharField(max_length=20, default="0000000000")
    email = models.EmailField(default="sucursal@ejemplo.com")

class Empleado(models.Model):
    nombre = models.CharField(max_length=100, default="Alejandro")
    apellido = models.CharField(max_length=100, default="Garcia")
    puesto = models.CharField(max_length=100, default="Empleado")
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True)
    telefono = models.CharField(max_length=20, default="0000000000")

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, default="Cliente")
    apellido = models.CharField(max_length=100, default="Apellido")
    email = models.EmailField(default="cliente@ejemplo.com")
    telefono = models.CharField(max_length=20, default="0000000000")
    direccion = models.TextField(default="Sin dirección")