from django.db import models

class CalculoBiseccion(models.Model):
    ecuacion = models.CharField(max_length=100)
    a = models.FloatField()
    b = models.FloatField()
    tolerancia = models.FloatField(default=0.0001)
    resultado = models.TextField()

    def __str__(self):
        return f"Bisección: {self.ecuacion}"
