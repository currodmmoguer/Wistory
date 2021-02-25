from django.db import models
from colorfield.fields import ColorField
from datetime import datetime


class Dinastia(models.Model):
    nombre = models.CharField(max_length=255)
    lugar = models.CharField(max_length=100, null=True, blank=True)
    color = ColorField(null=True, blank=True)
    def __str__(self):
        return self.nombre


class Cargo(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class TipoEvento(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    img = models.URLField(max_length=255)
    fecha_ini = models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento')
    ac_fini = models.BooleanField(default=False, verbose_name='Antes de cristo')
    fecha_fin = models.DateField(null=True, blank=True, verbose_name='Fecha de fallecimiento')
    ac_ffin = models.BooleanField(default=False, verbose_name='Antes de cristo')
    dinastia = models.ForeignKey(Dinastia, null=True, blank=True, on_delete=models.SET_NULL)
    cargo = models.ForeignKey(Cargo, null=True, blank=True, on_delete=models.SET_NULL)
    info = models.URLField(max_length=255, null=True, blank=True)
    padre = models.ForeignKey('self', null=True, blank=True, related_name='papa', on_delete=models.SET_NULL)
    madre = models.ForeignKey('self', related_name='mama', null=True, blank=True, on_delete=models.SET_NULL)
    fecha_create = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.nombre


class Evento(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_ini = models.DateField(null=True, blank=True, verbose_name='Fecha inicio')
    ac_fini = models.BooleanField(default=False, verbose_name='Antes de cristo')
    fecha_fin = models.DateField(null=True, blank=True, verbose_name='Fecha final')
    ac_ffin = models.BooleanField(default=False, verbose_name='Antes de cristo')
    lugar = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    info = models.URLField(max_length=255, null=True, blank=True)
    # Tipo (Guerra, Batalla, Boda...) Hacer un modelo con estas cosas
    tipo = models.ForeignKey(TipoEvento, null=True, blank=True, on_delete=models.SET_NULL)
    personas = models.ManyToManyField(Persona)
    fecha_create = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.nombre

class Epoca(models.Model):
    nombre = models.CharField(max_length=255)
    # Inicio -> tipo date, siglo...
    # Fin ->        ''

