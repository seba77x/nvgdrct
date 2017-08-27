from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=50)

class MallaCurricular(models.Model):
    annoMalla = models.IntegerField()

class MatriculaMalla(models.Model):
    numeroMatriculados = models.IntegerField()

class Asignatura(models.Model):
    nombre = models.CharField(max_length=50)
    codigoAsignatura = models.CharField(max_length=10)
    profesorAsignado = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    creditos = models.IntegerField()
    duracion = models.CharField(max_length=5)

class InstanciaAsignatura(models.Model):
    anno = models.IntegerField()
    semestre = models.IntegerField()

class InscripcionAsignatura(models.Model):
    inscripcion = models.CharField(max_length=5)

class EstadoInscripcion(models.Model):
    fin = models.CharField(max_length=5)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=15)
    Carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    codigoCarrera = models.IntegerField()
    annoIngreso = models.IntegerField()
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=15)
    email = models.EmailField()
