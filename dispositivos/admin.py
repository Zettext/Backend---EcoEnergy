from django.contrib import admin
from .models import Categoria, Zona, Dispositivo

admin.site.register([Categoria, Zona])

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'zona', 'consumo_maximo')
    list_filter = ('estado', 'categoria')
    search_fields = ('nombre',)
