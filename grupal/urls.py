from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from main import views

urlpatterns = [
    path('principal/', include('main.urls')),
    path('redirect/', TemplateView.as_view(template_name='redirect.html'), name='redireccionar'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('inicio/', include('accounts.urls')),
    path('inicio/', include('django.contrib.auth.urls')),
    #Pruebas
    path('a/', views.noti , name='registrar'),
    #Profesor
    path('principal/p/', TemplateView.as_view(template_name='principalP.html')),
    path('principal/p/ver/<str:prof>', views.verProf , name='ver'),
    path('principal/p/asesoria/<str:prof>/<str:alum>/<str:dia>/<str:lugar>/<str:inicio>/<str:fin>', views.citaReservadaProf , name='citaProfVer'),
    path('principal/p/asesoria/<str:prof>/<str:alum>/<str:dia>/<str:lugar>/<str:inicio>/<str:fin>/<str:estado>', views.citaReservadaProfCancel , name='citaProfVer'),
    path('principal/p/asesoria/aceptar/<str:asesoria>', views.citaAceptar , name='reserva'),
    path('principal/p/asesoria/noaceptar/<str:asesoria>', views.citaNoAceptar , name='reserva'),
    path('principal/p/asesoria/atendido/<str:asesoria>/<str:prof>/<str:alum>/<str:dia>/<str:lugar>/<str:inicio>/<str:fin>/<str:razon>', views.citaAtendida , name='reserva'),
    path('principal/p/guardarProf/<str:prof>', views.crearProf , name='reserva'),
    path('principal/p/verHistorial/<str:tipo>/<str:prof>', views.verHisAse , name='modificar'),
    path('principal/p/historial/ver/<str:sel>', views.verHisFil , name='modificar'),
    #administrador
    path('principal/a/', TemplateView.as_view(template_name='principala.html')),
    path('principal/a/guardarAdmin/<str:admin>', views.crearAdmin , name='administrador'),
    path('principal/a/crearAse/<str:admin>', views.crearAse , name='asesoria'),
    path('principal/a/asesoriaCrear/<str:prof>/<str:inicio>/<str:fin>/<str:dia>/<str:lugar>/<str:cod>', views.crearCita_simple , name='CrearAse'),
    path('principal/a/gestAse/<str:tipo>', views.verAse , name='modificar'),
    path('principal/a/gestAse/ver/<str:sel>', views.verAseFil , name='modificar'),
    path('principal/a/elimiAse/<str:cita>', views.elimiAse , name='eliminar'),
    path('principal/a/modAse/<str:cita>', views.modAse , name='eliminar'),
    path('principal/a/asesoriaMod/<str:prof>/<str:inicio>/<str:fin>/<str:dia>/<str:lugar>/<str:cod>/<str:codElimi>', views.modCita_simple , name='ModAse'),
]
