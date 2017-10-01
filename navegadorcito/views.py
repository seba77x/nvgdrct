from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def login(request):
	return render(request, 'login.html')

def home(request):
	return render(request, 'estudiante.html')


def login_acceder(request):
	if request.method == "POST":
		print ('*'*50)
		usuario=request.POST['user']
		password=request.POST['password']
		print(usuario)
		print(password)
		print ('*'*50)
		profesor=Profesor.objects.get(rut=usuario)
		print(profesor)
		if(Profesor.objects.get(rut=request.POST['user'])):
			if (profesor.password==request.POST['password']):
				asignatura=Asignatura.objects.filter(profesor=profesor)
				render(request,'profesor.html',{"asignatura":asignatura})
#		if(Estudiante.objects.get(rut)):
	else:
		return redirect ('/')



#def profesor(request,idProfesor):
#	profesor=Profesor.objects.get(pk=idProfesor)
#	asignatura=Asignatura.objects.filter(profesor=profesor)
#	inscritos=asignatura.inscritos.all()
#	return render(request,'index/profesor.html', {"asignatura":asignatura, "alumnos":inscritos })

#def vista_estudiante(request,idEstudiante)
#	estudiante=Estudiante.objects.get(pk=idEstudiante)
#	return render(request, '', {"estudiante"=estudiante})