from django import forms

class BiseccionForm(forms.Form):
    ecuacion = forms.CharField(label="Ecuación", max_length=100)
    a = forms.FloatField(label=" a = Límite inferior")
    b = forms.FloatField(label=" b = Límite superior")
    tolerancia = forms.FloatField(label="e = Tolerancia", initial=0.0001)