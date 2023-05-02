from rest_framework import serializers
from .models import Project 
from .models import Persona

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'nombre_usuario', 'producto', 'categoria', 'marca', 'precio', 'fecha')
        read_only_fields = ('fecha', )

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id', 'nombre', 'apellido', 'edad', 'fecha', 'email', 'telefono', 'direccion')
        read_only_fields = ('fecha', )