from django.shortcuts import render
from django.http import HttpResponse


def login(request):
	return render(request, 'login.html')

def home(request):
	return render(request, 'home.html')


def login_acceder(request, ):



#def profesor(request,idProfesor):
#	profesor=Profesor.objects.get(pk=idProfesor)
#	asignatura=Asignatura.objects.filter(profesor=profesor)
#	inscritos=asignatura.inscritos.all()
#	return render(request,'index/profesor.html', {"asignatura":asignatura, "alumnos":inscritos })

#def vista_estudiante(request,idEstudiante)
#	estudiante=Estudiante.objects.get(pk=idEstudiante)
#	return render(request, '', {"estudiante"=estudiante})