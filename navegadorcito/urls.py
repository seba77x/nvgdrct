from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login', views.login, name='login'),
    url(r'^user', views.home, name='home'),
    url(r'^acceder$', views.login_acceder, name='login_acceder')

    #url(r'^$', views.index, name='index'),
    #url(r'profesor/(?P<idProfesor>[0-9]+)$', views.profesor,name='profesor'),
]