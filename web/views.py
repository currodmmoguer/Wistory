from django.shortcuts import render

def index(request):
    return render(request, 'search.html', {})

def persona(request):
    return render(request, 'persona.html', {})


