from django.shortcuts import render
from rest_framework import viewsets
from webapp.models import Juego, Modalidad, Idioma, Genero
from webapp.serializers import JuegoSerializer,ModalidadSerializer,IdiomaSerializer,GeneroSerializer

# Create your views here.
class JuegoViewset(viewsets.ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer

class ModalidadViewset(viewsets.ModelViewSet):
    queryset = Modalidad.objects.all()
    serializer_class = ModalidadSerializer

class IdiomaViewset(viewsets.ModelViewSet):
    queryset = Idioma.objects.all()
    serializer_class = IdiomaSerializer

class GeneroViewset(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

def index(request):
    return render(request, "webapp/index.html")