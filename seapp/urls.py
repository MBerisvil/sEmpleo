from django.contrib import admin
from django.urls import path, include
from . import views


admin.site.site_header = "Servicio de Empleo"
admin.site.site_title = "Servicio de Empleo"
admin.site.index_title = "Servicio de Empleo"

urlpatterns = [
    path('', views.index, name='index.html'),
    path('base/', views.base, name='base.html'),
    path('persona/', views.persona, name='persona.html'),
    path('estudiorealizado/', views.estudiorealizado, name='estudiorealizado.html'),
    path('contacto/', views.contacto, name='contacto.html'),
    path('listadocandidatos/', views.listado_candidatos, name='listadocandidatos.html'),
    path('modificarpersona/<id>/', views.modificar_persona, name='modificarpersona.html'),
    path('registrarse/', views.registrarse, name='registrarse.html'),
    path('informacionadicional/', views.informacionadicional, name='informacionadicional.html'),
    path('experiencialaboral/', views.experiencialaboral, name='experiencialaboral.html'),
    

]