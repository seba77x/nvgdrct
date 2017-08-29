from django.contrib import admin
from .models import *

entities=[Carrera, MallaCurricular, MatriculaMalla, Asignatura, InstanciaAsignatura, InscripcionAsignatura, EstadoInscripcion, Estudiante, Profesor]
admin.site.register(entities)
# Register your models here.
