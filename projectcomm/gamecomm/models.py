from django.db import models

class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    respeto =  models.IntegerField()
    alimento = models.IntegerField()
	dinero = models.IntegerField()
	energia = models.IntegerField()
	dopamina = models.IntegerField()
	sueno = models.IntegerField()
	supmoral = models.IntegerField()
	soberbia = models.IntegerField()
	gula = models.IntegerField()
	avaricia = models.IntegerField()
	ira = models.IntegerField()
	lujuria = models.IntegerField()
	pereza = models.IntegerField()
	envidia = models.IntegerField()

class Historia(models.Model):
	titulo = models.CharField(max_length=30)
	texto = models.CharField(max_length=1024)
	opciones = [
        (opcion1, 'opcion1'),
        (opcion2, 'opcion2'),
        (opcion3, 'opcion3'),
        (opcion4, 'opcion4'),
    ]