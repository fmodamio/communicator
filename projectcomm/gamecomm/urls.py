from django.urls import path, include

from rest_framework import routers

from .viewsets import JugadorViewSet

route = routers.SimpleRouter()
route.register('jugador',JugadorViewSet)

urlpatterns = route.urls