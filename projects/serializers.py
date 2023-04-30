from rest_framework import serializers
from .models import Project 

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'nombre_usuario', 'producto', 'categoria', 'marca', 'precio', 'fecha')
        read_only_fields = ('fecha', )