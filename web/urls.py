from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('persona/<id>', views.persona, name="persona"),
    path('ajax/ayud_persona', views.get_personas, name='get_personas'),
    path('ajax/dinastias_id', views.get_dinastias_by_id, name="get_dinastia_by_id"),
    path('ajax/dinastias', views.get_dinastias, name="get_dinastias"),
    path('ajax/cargos', views.get_cargos, name="get_cargos"),
    path('ajax/eventos', views.get_eventos, name="get_eventos"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)