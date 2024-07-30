from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request,"cenmed/index.html") 

def medicos(request):
    return HttpResponse ("Esta es la vista de Medicos")

def pacientes(request):
    return HttpResponse ("Esta es la vista de Pacientess")

def habitaciones(request):
    return HttpResponse ("Esta es la vista de habitaciones")

def medicamentos(request):
    return HttpResponse ("Esta es la vista de Medicamentos")