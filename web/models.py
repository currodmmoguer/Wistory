from django.db import models
from colorfield.fields import ColorField
from datetime import datetime


class Dinastia(models.Model):
    nombre = models.CharField(max_length=255)
    lugar = models.CharField(max_length=100, null=True, blank=True)
    color = ColorField(null=True, blank=True)

    class Meta:
        db_table = 'dinastia'
        verbose_name = 'Dinastía'
        verbose_name_plural = 'Dinastías'
    
    def __str__(self):
        return self.nombre


class Cargo(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'cargo'
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
    

    def __str__(self):
        return self.nombre

class TipoEvento(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'tipo_evento'
        verbose_name = 'Tipo de evento'
        verbose_name_plural = 'Tipos de eventos'

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
    info = models.URLField(max_length=255, null=True, blank=True)
    padre = models.ForeignKey('self', null=True, blank=True, related_name='papa', on_delete=models.SET_NULL)
    madre = models.ForeignKey('self', related_name='mama', null=True, blank=True, on_delete=models.SET_NULL)
    fecha_create = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'persona'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return self.nombre

class Persona_Cargo(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="cargos")
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name="personas")
    fecha_ini = models.DateField(verbose_name='Fecha inicio')
    ac_fini = models.BooleanField(default=False, verbose_name='Antes de cristo')
    fecha_fin = models.DateField(null=True, blank=True, verbose_name='Fecha fin')
    ac_ffin = models.BooleanField(default=False, verbose_name='Antes de cristo')

    class Meta:
        db_table = 'rel_persona_cargo'
        verbose_name = 'Relación persona y cargo'
        verbose_name_plural = 'Relaciones de personas y cargos'

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

    class Meta:
        db_table = 'evento'
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.nombre

class Relacion_Persona(models.Model):
    persona1 = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="persona1")
    persona2 = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="persona2")
    motivo = models.CharField(max_length=255)

    class Meta:
        db_table = 'rel_personas'
        verbose_name = 'Relacion entre personas'
        verbose_name_plural = 'Relaciones entre personas'

class Epoca(models.Model):
    nombre = models.CharField(max_length=255)
    siglo_inicio = models.IntegerField(default=0)
    siglo_fin = models.IntegerField(default=0)
    fecha_ini = models.DateField(null=True, blank=True, verbose_name='Fecha inicio')
    ac_fini = models.BooleanField(default=False, verbose_name='Antes de cristo')
    fecha_fin = models.DateField(null=True, blank=True, verbose_name='Fecha final')
    ac_ffin = models.BooleanField(default=False, verbose_name='Antes de cristo')

    class Meta:
        db_table = 'epoca'
        verbose_name = 'Época'
        verbose_name_plural = 'Épocas'

