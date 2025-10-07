from django.contrib import admin
from django.urls import path

from dispositivos.views import inicio, dispositivos, crear_dispositivo, editar_dispositivo, eliminar_dispositivo, listar_dispositivos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('dispositivos/', listar_dispositivos, name="listar_dispositivos"),
    path('dispositivos/<int:dispositivo_id>/', dispositivos, name="dispositivo"),
    path('dispositivos/crear/', crear_dispositivo, name="crear_dispositivo"),

    path('dispositivos/editar/<int:dispositivo_id>/', editar_dispositivo, name="editar_dispositivo"),
    path('dispositivos/eliminar/<int:dispositivo_id>/', eliminar_dispositivo, name="eliminar_dispositivo"),
]
