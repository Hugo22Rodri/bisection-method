from django import forms

class BiseccionForm(forms.Form):
    ecuacion = forms.CharField(label="Ecuación", max_length=100)
    a = forms.FloatField(label="Límite inferior")
    b = forms.FloatField(label="Límite superior")
    tolerancia = forms.FloatField(label="Tolerancia", initial=0.0001)
