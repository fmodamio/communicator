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

	def __str__(self):
		return self.nombre

class Historia(models.Model):
	titulo = models.CharField(max_length=30)
	texto = models.CharField(max_length=1024)

	def __str__(self):
		return self.titulo