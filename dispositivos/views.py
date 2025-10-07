from django.shortcuts import render

# Create your views here.
#FORMA FACIL DE HACER UN "PRINT" EN DJANGO
from django.http import HttpResponse
from .models import Dispositivo

def inicio(request):
    #contexto = {"nombre": "Javier Sanchez"}
    dispositivos = Dispositivo.objects.select_related("categoria")

    return render(request, "dispositivos/panel.html", {"dispositivos": dispositivos})