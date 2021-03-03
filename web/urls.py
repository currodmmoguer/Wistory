from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('persona', views.persona, name="persona"),
    path('ajax/ayud_persona', views.get_personas, name='get_personas'),
    path('ajax/dinastia', views.get_dinastia, name="get_dinastia"),
    path('ajax/cargos', views.get_cargos, name="get_cargos"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)