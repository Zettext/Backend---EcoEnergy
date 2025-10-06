from django.shortcuts import render

# Create your views here.
#FORMA FACIL DE HACER UN "PRINT" EN DJANGO
from django.http import HttpResponse

def inicio(request):
    #contexto = {"nombre": "Javier Sanchez"}
    dispositivos = [
        {"nombre": "Sensor de Temperatura", "consumo": 50, "estado": "x"},
        {"nombre": "Medidor Solar", "consumo": 120, "estado": "x"},
        {"nombre": "Sensor de Movimiento", "consumo": 30, "estado": "x"},
        {"nombre": "Calefactor", "consumo": 200, "estado": "x"},
    ]

    consumo_maximo = 100
    for i in range(len(dispositivos)):
        if dispositivos[i]["consumo"] > consumo_maximo:
            dispositivos[i]["estado"] = "Exceso"
        elif dispositivos[i]["consumo"] <= consumo_maximo:
            dispositivos[i]["estado"] = "Correcto"
    return render(request, "dispositivos/panel.html", {
        "dispositivos": dispositivos,
        "consumo_maximo": consumo_maximo
    })