import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .models import *

def index(request):
    return render(request, 'index.html', {})

def persona(request):
    return render(request, 'person.html', {})

# AJAX

def ayuda_busqueda_persona(request):
    personas = Persona.objects.all()
    tmpJson = serializers.serialize("json",personas)
    tmpObj = json.loads(tmpJson)
    return HttpResponse(json.dumps(tmpJson))

