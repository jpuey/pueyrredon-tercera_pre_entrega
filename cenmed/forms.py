from django import forms


class MedicoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    matricula = forms.IntegerField()
    especialidad= forms.CharField(max_length=30)
    email= forms.EmailField()


class PacienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    identificacion= forms.IntegerField()
    email= forms.EmailField()
    habitacion = forms.IntegerField()


class HabitacionFormulario(forms.Form):
    numero = forms.IntegerField()
    ocupado= forms.BooleanField()


class MedicamentoFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    inventario= forms.IntegerField()
    requiere_receta= forms.BooleanField()