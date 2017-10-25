# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from .models import *

# Register your models here.
class PrevencionAdmin(admin.ModelAdmin):
	list_display=('tipo','descripcion')

admin.site.register(Prevencion,PrevencionAdmin)