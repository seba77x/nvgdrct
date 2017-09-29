from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'profesor/(?P<idProfesor>[0-9]+)$', views.profesor,name='profesor'),
]