from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=15)
    Carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    codigoCarrera = models.IntegerField()
    annoIngreso = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class MallaCurricular(models.Model):
    annoMalla = models.IntegerField()
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.carrera)+" "+str(self.annoMalla)


class MatriculaMalla(models.Model):
    numeroMatriculados = models.IntegerField()
    mallacurricular = models.ForeignKey(MallaCurricular, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return self.numeroMatriculados


class Asignatura(models.Model):
    nombre = models.CharField(max_length=50)
    codigoAsignatura = models.CharField(max_length=10)
    profesorAsignado = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    creditos = models.IntegerField()
    duracion = models.CharField(max_length=5)
    mallacurricular = models.ForeignKey(MallaCurricular, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class InscripcionAsignatura(models.Model):
    inscripcion = models.CharField(max_length=5)
    anno = models.IntegerField()
    semestre = models.IntegerField()
    fin = models.CharField(max_length=5)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return self.inscripcion




