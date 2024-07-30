from django.db import models

# Create your models here.

class Medico(models.Model):
    nombre = models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    matricula = models.IntegerField()
    especialidad= models.CharField(max_length=30)
    email= models.EmailField()
    def __str__(self) :
        return f"Nombre del Profesional: {self.nombre} - Apellido del Profesional: {self.apellido} - Numero de Matricula: {self.matricula} - Especialidad: {self.especialidad} - Correo electronico {self.email}"


class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    identificacion= models.IntegerField()
    email= models.EmailField()
    habitacion = models.IntegerField()
    def __str__(self):
        return f"Nombre del Paciente: {self.nombre} - Apellido del Paciente: {self.apellido} - Numero de identificacion del Paciente: {self.identificacion} - Correo electronico: {self.email} - Numero de Habitacion: {self.habitacion}"

class Habitacion(models.Model):
    numero = models.IntegerField()
    ocupado= models.BooleanField()
    def __str__(self):
        return f"Numero de Habitacion: {self.numero} - Ocupación: {self.ocupado}"

class Medicamento(models.Model):
    nombre= models.CharField(max_length=30)
    inventario= models.IntegerField()
    requiere_receta= models.BooleanField()
    def __str__(self):
        return f"Nombre del Medicamento: {self.nombre} - Numero de Inventario: {self.inventario} - Requiere Receta: {self.requiere_receta} "