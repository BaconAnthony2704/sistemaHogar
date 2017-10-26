# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from .models import *

# Register your models here.
class PrevencionAdmin(admin.ModelAdmin):
	list_display=('tipo','descripcion','medidas')
class ServicioAdmin(admin.ModelAdmin):
	list_display=('tipo','contenido','nombre_imagen')

admin.site.site_header='Sitio administrativo de seguridad del hogar'
admin.site.register(Prevencion,PrevencionAdmin)
admin.site.register(Servicio,ServicioAdmin)
