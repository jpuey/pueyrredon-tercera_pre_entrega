from django.contrib import admin

from .models import *

class MedicoAdmin(admin.ModelAdmin):
    list_display= ("nombre", "apellido", "matricula", "especialidad", "email")
    list_filter= ("nombre",)

class PacienteAdmin(admin.ModelAdmin):
    list_display= ("nombre", "apellido", "identificacion", "email", "habitacion")
    list_filter= ("nombre",)

class MedicamentoAdmin(admin.ModelAdmin):
    list_display= ("nombre", "inventario", "requiere_receta")
    list_filter= ("nombre",)

class HabitacionAdmin(admin.ModelAdmin):
    list_display= ("numero", "ocupado")
    list_filter= ("nombre",)

# Register your models here.
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Medicamento, MedicamentoAdmin)
admin.site.register(Habitacion, HabitacionAdmin)