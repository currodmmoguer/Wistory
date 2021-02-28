from django.contrib import admin
from django.apps import apps


app = apps.get_app_config('web')
for model_name, model in app.models.items():
    admin.site.register(model)

# admin.site.register(models.Dinastia)
# admin.site.register(models.Evento)
# admin.site.register(models.TipoEvento)
# admin.site.register(models.Cargo)
