from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def profesor(request,idProfesor):
	profesor=Profesor.objects.get(pk=idProfesor)
	asignatura=Asignatura.objects.filter(profesor=profesor)
	inscritos=asignatura.inscritos.all()
	return render(request,'index/profesor.html', {"asignatura":asignatura, "alumnos":inscritos })

