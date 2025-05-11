from django.urls import path
from BiseccionApp.views.w_views import calcular
from BiseccionApp.views.a_views import BiseccionAPI

urlpatterns = [
    path("calculo/", calcular, name="calculo"),
    path("api/biseccion/", BiseccionAPI.as_view(), name="biseccion-api"),
]
