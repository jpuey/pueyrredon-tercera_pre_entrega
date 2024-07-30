from django.db import models

# Create your models here.

class Medico(models.Model):
    nombre = models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    matricula = models.IntegerField()
    especialidad= models.CharField(max_length=30)
    email= models.EmailField()

class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    identificacion= models.IntegerField()
    email= models.EmailField()
    habitacion = models.IntegerField()

class Habitacion(models.Model):
    numero = models.IntegerField()
    ocupado= models.BooleanField()

class Medicamento(models.Model):
    nombre= models.CharField(max_length=30)
    inventario= models.IntegerField()
    requiere_receta= models.BooleanField()