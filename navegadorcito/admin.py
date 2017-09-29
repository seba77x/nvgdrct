from django.contrib import admin
from .models import *

entities=[Carrera, MallaCurricular, MatriculaMalla, Asignatura, InscripcionAsignatura, Estudiante, Profesor]
admin.site.register(entities)
# Register your models here.
