from rest_framework import serializers
from .models import Jugador, Historia

import bleach

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = ['id','nombre']

    def create(self, validated_data):
        nombrepost = bleach.clean(validated_data.pop('nombre'))

        #esto hay que cambiarlo en el modelo, usando default
        return Jugador.objects.create(nombre=nombrepost,respeto = 1, alimento = 1, dinero = 1, energia = 1, dopamina = 1, sueno = 1,
    supmoral = 1, soberbia = 1, gula = 1, avaricia = 1, ira = 1, lujuria = 1, pereza = 1, envidia = 1)

class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = '__all__'