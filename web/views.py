import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .models import *
from django.shortcuts import get_object_or_404

#Contains
from django.db.models import Q


def index(request):
    personas = Persona.objects.all()[:4]
    eventos = Evento.objects.all()[:4]
    data = {
        'personas': personas,
        'eventos': eventos,
    }
    return render(request, 'index.html', data)


def persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    return render(request, 'person.html', {'persona': persona})

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

def get_dinastias(request):
    dic_dinastias = {}
    dinastias = Dinastia.objects.filter(Q(nombre__icontains=request.GET['nombre']))

    for dinastia in dinastias:
        dic_dinastias[dinastia.pk] = dinastia.nombre

    return JsonResponse(dic_dinastias)

# Obtiene las dinastías a partir de una lista de IDs
def get_dinastias_by_id(request):
    dic_dinastias = {}
    lista = dict(request.GET.lists())['id[]']
    
    for i in range(0, len(lista)): 
        lista[i] = int(lista[i])

    dinastias = Dinastia.objects.filter(pk__in=lista)
    
    for dinastia in dinastias:
        dic_dinastias[dinastia.pk] = dinastia.nombre

    return JsonResponse(dic_dinastias)

# Obtiene los cargos a partir de una lista de IDs
def get_cargos(request):
    dic_cargos = {}
    lista = dict(request.GET.lists())['id[]']
    for i in range(0, len(lista)): 
        lista[i] = int(lista[i])

    cargos = Persona_Cargo.objects.filter(persona__pk__in=lista)
    
    for cargo in cargos:
        dic_cargos[cargo.persona.pk] = cargo.cargo.nombre
    
    return JsonResponse(dic_cargos)

# Obtiene los eventos a partir de un nombre
def get_eventos(request):
    dic_eventos = {}
    eventos = Evento.objects.filter(nombre__in=request.GET['nombre'])
    
    for evento in eventos:
        dic_eventos[evento.pk] = evento.nombre

    return JsonResponse(dic_eventos)