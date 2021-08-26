from rest_framework import viewsets

from rest_framework.throttling import ScopedRateThrottle

from .models import Jugador, Historia
from .serializer import JugadorSerializer, HistoriaSerializer

class JugadorViewSet(viewsets.ModelViewSet):
	queryset = Jugador.objects.all()
	serializer_class = JugadorSerializer
	def get_throttles(self):
		if self.action in ['create']:
		    self.throttle_scope = 'foo.' + self.action
		return super().get_throttles()

class HistoriaViewSet(viewsets.ModelViewSet):
	queryset = Historia.objects.all()
	serializer_class = HistoriaSerializer
	#http_method_names = ['get']