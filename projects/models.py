from django.db import models

# Create your models here.
class Project(models.Model):
    nombre_usuario = models.CharField(max_length=200)
    producto = models.CharField(max_length=100, default='')
    categoria = models.TextField()
    marca = models.CharField(max_length=205)
    precio = models.CharField(max_length=170, default='0.00')
    fecha = models.DateTimeField(auto_now_add=True)
    
class Persona(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=90)
    edad = models.CharField(max_length=50, default='')
    fecha = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)

class Categoria(models.Model):
    nombre = models.CharField(max_length=80)
    cantidad_productos = models.IntegerField()
    fecha_recepcion = models.DateTimeField(auto_now_add=True)
    valor = models.CharField(max_length=90)

class Sucursales(models.Model):
    nombre = models.CharField(max_length=80)
    direccion = models.CharField(max_length=90)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    fecha_apertura = models.DateTimeField(auto_now_add=True)
    cantidad_empleados = models.IntegerField()

class Vendedor(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=90)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    productos_vendidos = models.IntegerField()
    fecha_ingreso = models.DateTimeField(auto_now_add=True)

class Empleados(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=90)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    sueldo = models.CharField(max_length=90)
    cargo = models.CharField(max_length=80)

class Productos(models.Model):
    nombre = models.CharField(max_length=80)
    categoria = models.CharField(max_length=200)
    marca = models.CharField(max_length=90)
    precio = models.CharField(max_length=20)
    categoria = models.CharField(max_length=200)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()
    sucursal = models.CharField(max_length=80)
    proveedor = models.CharField(max_length=90)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=80)
    apellido_paterno = models.CharField(max_length=90)
    apellido_materno = models.CharField(max_length=90)
    edad = models.IntegerField()
    Productos_proveidos = models.CharField(max_length=200)
    marcas = models.CharField(max_length=200)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
