# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Prevencion(models.Model):
	tipo=models.CharField(max_length=50,unique=True)
	descripcion=models.TextField(max_length=600)
	class Meta:
		verbose_name='Prevencion'
		verbose_name_plural='Prevenciones'
	def __str__(self):
		return '%s' %(self.tipo)