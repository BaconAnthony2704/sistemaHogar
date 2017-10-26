# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from .models import *
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

# Register your models here.
class PrevencionAdmin(admin.ModelAdmin):
	list_display=('tipo','descripcion')
class ServicioAdmin(admin.ModelAdmin):
	list_display=('tipo','contenido','nombre_imagen')
class MedidaAdmin(admin.ModelAdmin):
	list_display=('tipo','descripcion')
#class NormaAdmin(admin.ModelAdmin):
#	model=Norma
#	filter_horizontal=('codigo',)
class NormaAdmin(admin.ModelAdmin):
	list_display=('codigo','estandar','tipo','fundamento')

admin.site.site_header='Sitio administrativo de seguridad del hogar'
admin.site.register(Prevencion,PrevencionAdmin)
admin.site.register(Servicio,ServicioAdmin)
admin.site.register(Medida,MedidaAdmin)
admin.site.register(Norma,NormaAdmin)
#admin.site.register(Norma)
#admin.site.register()