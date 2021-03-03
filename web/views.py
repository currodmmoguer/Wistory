import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .models import *
# from django.shortcuts import get_object_or_404

#Contains
from django.db.models import Q


def index(request):
    return render(request, 'index.html', {})


def persona(request):
    return render(request, 'person.html', {})

# AJAX


def get_personas(request):
    personas = Persona.objects.filter(Q(nombre__icontains=request.GET['nombre']))
    dinastias = Dinastia.objects.filter(Q(nombre__icontains=request.GET['dinastia']))
    cargos = Cargo.objects.filter(Q(nombre__icontains=request.GET['cargo']))
    pers_cargo = Persona_Cargo.objects.filter(cargo__in=cargos)
    lista = []

    # En caso de solo haber un campo relleno
    if not request.GET['dinastia'] and not request.GET['cargo']:
        lista = personas
    elif not request.GET['nombre'] and not request.GET['cargo']:
        lista = Persona.objects.filter(dinastia__in=dinastias)
    elif not request.GET['nombre'] and not request.GET['dinastia']:
        lista = Persona.objects.filter(cargos__in=pers_cargo)

    if not lista:
        if personas:    
            if dinastias:
                lista = personas.filter(dinastia__in=dinastias)
            if cargos:
                lista = personas.filter(cargos__in=pers_cargo)
        else:   # En caso de que no se haya introducido nombre, tiene que filtrarse por dinastía y cargo
            lista = Persona.objects.filter(dinastia__in=dinastias)
            lista = lista.filter(cargos__in=pers_cargo)

    tmpJson = serializers.serialize("json", lista)
    tmpObj = json.loads(tmpJson)
    return JsonResponse({'personas': tmpObj})


# Obtiene las dinastías a partir de una lista de IDs
def get_dinastia(request):
    dic_dinastias = {}
    lista = dict(request.GET.lists())['id[]']
    
    for i in range(0, len(lista)): 
        lista[i] = int(lista[i])

    dinastias = Dinastia.objects.filter(pk__in=lista)
    
    for dinastia in dinastias:
        dic_dinastias[dinastia.pk] = dinastia.nombre

    return JsonResponse(dic_dinastias)

def get_cargos(request):
    dic_cargos = {}
    lista = dict(request.GET.lists())['id[]']
    for i in range(0, len(lista)): 
        lista[i] = int(lista[i])

    cargos = Persona_Cargo.objects.filter(persona__pk__in=lista)
    
    for cargo in cargos:
        dic_cargos[cargo.persona.pk] = cargo.cargo.nombre
    
    return JsonResponse(dic_cargos)

