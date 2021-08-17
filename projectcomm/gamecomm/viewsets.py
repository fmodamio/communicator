from rest_framework import viewsets

from .models import Jugador, Historia
from .serializer import JugadorSerializer, HistoriaSerializer

class JugadorViewSet(viewsets.ModelViewSet):
	queryset = Jugador.objects.all()
	serializer_class = JugadorSerializer
	http_method_names = ['get']

class HistoriaViewSet(viewsets.ModelViewSet):
	queryset = Historia.objects.all()
	serializer_class = HistoriaSerializer