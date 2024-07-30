from django.urls import path
from cenmed.views import *

urlpatterns = [
    path("", inicio, name="index"),
    path("medicos", medicos, name= "medicos"),
    path("pacientes", pacientes, name= "pacientes"),
    path("habitaciones", habitaciones, name= "habitaciones"),
    path("medicamentos", medicamentos, name= "medicamentos"),
]


