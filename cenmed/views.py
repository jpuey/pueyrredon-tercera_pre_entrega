from django.shortcuts import render
from django.http import HttpResponse

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