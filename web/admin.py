from django.contrib import admin

from .import models

admin.site.register(models.Persona)
admin.site.register(models.Dinastia)
admin.site.register(models.Evento)
admin.site.register(models.TipoEvento)
admin.site.register(models.Cargo)
