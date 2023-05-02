from .models import Project
from .models import Persona
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer
from .serializers import PersonaSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonaSerializer
   