from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
#FORMA FACIL DE HACER UN "PRINT" EN DJANGO
from django.http import HttpResponse
from .models import Dispositivo
from .forms import DispositivoForm

def inicio(request):
    #contexto = {"nombre": "Javier Sanchez"}
    dispositivos = Dispositivo.objects.select_related("categoria")

    return render(request, "dispositivos/panel.html", {"dispositivos": dispositivos})

def dispositivos(request, dispositivo_id): #SOLUCIONAR
    dispositivo = Dispositivo.objects.get(id=dispositivo_id)
    if request.method == "POST":
        form = DispositivoForm(request.POST, instance=dispositivo)
        if form.is_valid():
            form.save()
    else:
        form = DispositivoForm(instance=dispositivo)

    return render(request, "dispositivos/detalle.html", {"dispositivo": dispositivo, "form": form})


def listar_dispositivos(request):
    dispositivos = Dispositivo.objects.all()
    return render(request, "dispositivos/listar.html", {"dispositivos": dispositivos})

def crear_dispositivo(request):
    if request.method == "POST":
        form = DispositivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_dispositivos')
    else:
        form = DispositivoForm()

    return render(request, "dispositivos/crear.html", {"form": form})

def editar_dispositivo(request, dispositivo_id):
    dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id)
    if request.method == "POST":
        form = DispositivoForm(request.POST, instance=dispositivo)
        if form.is_valid():
            form.save()
            return redirect('listar_dispositivos')
    else:
        form = DispositivoForm(instance=dispositivo)

    return render(request, "dispositivos/editar.html", {"form": form, "dispositivo": dispositivo})

def eliminar_dispositivo(request, dispositivo_id):
    dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id)
    if request.method == "POST":
        dispositivo.delete()
        return redirect('listar_dispositivos')
    return render(request, "dispositivos/eliminar.html", {"dispositivo": dispositivo})