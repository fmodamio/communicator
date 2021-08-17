from rest_framework import serializers
from .models import Jugador, Historia

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = '__all__'

class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = '__all__'