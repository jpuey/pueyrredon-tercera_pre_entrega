from django.urls import path
from cenmed.views import *

urlpatterns = [
    path("", inicio, name="index"),
    path("medicos", medicos, name= "medicos"),
    path("pacientes", pacientes, name= "pacientes"),
    path("habitaciones", habitaciones, name= "habitaciones"),
    path("medicamentos", medicamentos, name= "medicamentos"),
    path("form-medico", medicoFormulario, name="form-medico"),
    path("form-habi", habitacionFormulario, name="form-habi"),
    path("form-pacientes", pacientesFormulario, name="form-pacientes"),
    path("form-meds", medsFormulario, name="form-meds"),
    path("busquedaPaciente", busquedaPaciente, name= "BusquedaPaciente"),
    path("buscar", buscar)
]


