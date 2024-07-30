from django.shortcuts import render
from django.http import HttpResponse
from cenmed.forms import *
from cenmed.models import *


# Create your views here.
def inicio(request):
    return render(request,"cenmed/index.html") 

def medicos(request):
    return render(request,"cenmed/medicos.html")

def pacientes(request):
    return render(request,"cenmed/pacientes.html")

def habitaciones(request):
    return render(request,"cenmed/habitaciones.html")

def medicamentos(request):
    return render(request, "cenmed/medicamentos.html")


def medicoFormulario(request):

    if request.method == "POST":

            miFormulario = MedicoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                medico = Medico(nombre=informacion["nombre"], apellido =informacion["apellido"], matricula=informacion["matricula"], especialidad=informacion["especialidad"], email=informacion["email"] )
                medico.save()
                return render(request, "cenmed/medicos.html")
    else:
            miFormulario = MedicoFormulario()

    return render(request, "cenmed/form-medico.html", {"miFormulario": miFormulario})


def habitacionFormulario(request):

    if request.method == "POST":

            FormularioHabi = HabitacionFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                habitacion = Habitacion(nummero=informacion["numero"], ocupado =informacion["ocupado"])
                habitacion.save()
                return render(request, "cenmed/habitaciones.html")
    else:
            miFormulario = HabitacionFormulario()

    return render(request, "cenmed/form-habi.html", {"miFormulario": miFormulario})


def pacientesFormulario(request):

    if request.method == "POST":

            miFormulario = PacienteFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                paciente = Paciente(nombre=informacion["nombre"], apellido =informacion["apellido"], identificacion=informacion["identificacion"], habitacion=informacion["habitacion"], email=informacion["email"] )
                paciente.save()
                return render(request, "cenmed/pacientes.html")
    else:
            miFormulario = PacienteFormulario()

    return render(request, "cenmed/form-pacientes.html", {"miFormulario": miFormulario})



def medsFormulario(request):

    if request.method == "POST":

            FormularioHabi = MedicamentoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                meds = Medicamento(nombre=informacion["nombre"], inventario =informacion["Numero de inventario"], requiere_receta=informacion["requiere receta"])
                meds.save()
                return render(request, "cenmed/medicamentos.html")
    else:
            miFormulario = MedicamentoFormulario()

    return render(request, "cenmed/form-meds.html", {"miFormulario": miFormulario})

def busquedaPaciente (request):
    return render (request, "cenmed/busquedaPaciente.html")

def buscar(request):
    respuesta= f"Estoy buscando al Paciente con numero de identificacion: {request.GET ["identificacion"]}"
    return HttpResponse(respuesta)