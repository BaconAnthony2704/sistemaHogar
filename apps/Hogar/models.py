# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Prevencion(models.Model):
	tipo=models.CharField(max_length=50,unique=True)
	descripcion=models.TextField(max_length=600)
	#medidas=models.TextField(max_length=300)
	class Meta:
		verbose_name='Prevencion'
		verbose_name_plural='Prevenciones'
	def __str__(self):
		return '%s' %(self.tipo)

class Servicio(models.Model):
	tipo=models.CharField(max_length=50,unique=True)
	contenido=models.TextField(max_length=300)
	nombre_imagen=models.CharField(max_length=20)
	class Meta:
		verbose_name='Servicio'
		verbose_name_plural='Servicios'
	def __str__(self):
		return '%s' %(self.tipo)


class Medida(models.Model):
	tipo=models.ForeignKey(Prevencion)
	descripcion=models.CharField(max_length=300)
	class Meta:
		verbose_name='Medida'
		verbose_name_plural='Medidas'
	def __str__(self):
		return '%s' %(self.tipo)

class Norma(models.Model):
	codigo=models.CharField(max_length=15,unique=True)
	estandar=models.CharField(max_length=150)
	tipo=models.ForeignKey(Prevencion)
	fundamento=models.TextField(max_length=800)
	#def tipo_asociados(self):
	#	return "\n".join([i.tipo for i in self.tipo.all()])

	class Meta:
		verbose_name='Norma'
		verbose_name_plural='Normas'
	def __str__(self):
		return '%s' %(self.codigo)
