from django.urls import path, include

from rest_framework import routers

from .viewsets import JugadorViewSet, HistoriaViewSet

route = routers.SimpleRouter()
route.register('player',JugadorViewSet)
route.register('game',HistoriaViewSet)

urlpatterns = route.urls