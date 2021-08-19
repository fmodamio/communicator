from rest_framework import serializers
from .models import Jugador, Historia

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = ['nombre']

    def create(self, validated_data):
        profile_data = validated_data.pop('nombre')
        user = Jugador.objects.create(nombre=profile_data,respeto = 1, alimento = 1, dinero = 1, energia = 1, dopamina = 1, sueno = 1,
    supmoral = 1, soberbia = 1, gula = 1, avaricia = 1, ira = 1, lujuria = 1, pereza = 1, envidia = 1, )
        return user

class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = '__all__'