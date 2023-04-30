from django.db import models

# Create your models here.
class Project(models.Model):
    nombre_usuario = models.CharField(max_length=200)
    producto = models.CharField(max_length=100, default='')
    categoria = models.TextField()
    marca = models.CharField(max_length=200)
    precio = models.CharField(max_length=170, default='0.00')
    fecha = models.DateTimeField(auto_now_add=True)
    
