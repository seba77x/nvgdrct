from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=50)

        def__str__(self):
            return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=15)
    Carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    codigoCarrera = models.IntegerField()
    annoIngreso = models.IntegerField()
    email = models.EmailField()

        def__str__(self):
            return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=15)
    email = models.EmailField()

        def__str__(self):
            return self.nombre


class MallaCurricular(models.Model):
    annoMalla = models.IntegerField()
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

        def__str__(self):
            return str(self.nombre)+" "+str(self.carrera)


class MatriculaMalla(models.Model):
    numeroMatriculados = models.IntegerField()
    mallacurricular = models.ForeignKey(MallaCurricular, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

        def__str__(self):
            return self.numeroMatriculados


class Asignatura(models.Model):
    nombre = models.CharField(max_length=50)
    codigoAsignatura = models.CharField(max_length=10)
    profesorAsignado = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    creditos = models.IntegerField()
    duracion = models.CharField(max_length=5)
    mallacurricular = models.ForeignKey(MallaCurricular, on_delete=models.CASCADE)
    inscritos = models.ManytoManyField(Estudiante,through='InscripcionAsignatura')

        def__str__(self):
            return self.nombre


class InstanciaAsignatura(models.Model):
    anno = models.IntegerField()
    semestre = models.IntegerField()
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

        def__str__(self):
            return "Semestre:"+str(self.semestre)+", Año: "+str(self.anno)


class EstadoInscripcion(models.Model):
    fin = models.CharField(max_length=5)

        def__str__(self):
            return self.fin


class InscripcionAsignatura(models.Model):
    inscripcion = models.CharField(max_length=5)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    estadoinscripcion = models.ForeignKey(EstadoInscripcion, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

        def__str__(self):
            return self.inscripcion




