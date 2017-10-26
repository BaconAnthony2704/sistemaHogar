# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.http import Http404
from django.core.paginator import Paginator,InvalidPage,EmptyPage
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import socket
import time
from django.db.models import Count

# Create your views here.
def index(request):
	servicio=Servicio.objects.all()
	return render(request,'index.html',{'servicio':servicio})

def prevencion(request):
	prevencion=Prevencion.objects.all()
	return render(request,'prevencion.html',{'prevencion':prevencion})

def normas(request):
	return render(request,'normas.html',{})