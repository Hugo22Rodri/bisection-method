from django.shortcuts import render
from BiseccionApp.forms import BiseccionForm
from BiseccionApp.utils.calculations import biseccion
from BiseccionApp.utils.plotting import graficar_convergencia
from BiseccionApp.models import CalculoBiseccion
import json

def calcular(request):
    pasos = []
    if request.method == "POST":
        form = BiseccionForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            resultado = biseccion(datos)
            pasos = resultado["pasos"]  # Extrae solo los pasos

            # Guardar en la base de datos
            CalculoBiseccion.objects.create(
                ecuacion=datos["ecuacion"],
                a=datos["a"],
                b=datos["b"],
                tolerancia=datos["tolerancia"],
                resultado=json.dumps(pasos)  # Guarda los pasos como JSON
            )

            # Genera la gráfica
            graficar_convergencia(pasos)

    else:
        form = BiseccionForm()

    return render(request, "BiseccionApp/calculo.html", {"form": form, "pasos": pasos, "grafica_url": "/static/biseccion.png"})