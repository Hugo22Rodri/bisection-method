from django.urls import path
from django.views.generic.base import RedirectView
from BiseccionApp.views.w_views import calcular
from BiseccionApp.views.a_views import BiseccionAPI

urlpatterns = [
    path("", RedirectView.as_view(url='calculo/', permanent=True), name='index'),
    path("calculo/", calcular, name="calculo"),
    path("api/biseccion/", BiseccionAPI.as_view(), name="biseccion-api"),
]
