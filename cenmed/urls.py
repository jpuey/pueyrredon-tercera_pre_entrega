from django.urls import path
from cenmed.views import *

urlpatterns = [
    path("", inicio),
    path("medicos", medicos),
    path("pacientes", pacientes),
    path("habitaciones", habitaciones),
    path("medicamentos", medicamentos),
]


