from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    #Alumno
    path('', views.princ , name='principal'),
    path('busqueda1/', views.busqueda1 , name='busqueda1'),
    path('busqueda1/<str:ca>/<str:prof>', views.busqueda1_Cu , name='busqueda1_Cu'),
    path('buscar1/<str:car>/<str:profe>/<str:cur>/<str:usu>', views.busqueda1_real , name='buscar1'),
    path('busqueda2/', views.busq2 , name='busqueda2'),
    path('busqueda2/<str:etiq>/<str:usu>', views.busqueda2_real , name='busqueda2'),
    path('asesoria/<str:prof>/<str:alum>/<str:dia>/<str:lugar>/<str:inicio>/<str:fin>', views.citaReservada , name='reserva'),
    path('asesoria/<str:prof>/<str:alum>/<str:dia>/<str:lugar>/<str:inicio>/<str:fin>/<str:estado>', views.citaReservadaCancel , name='reserva'),
    path('asesoria/ver/aceptado/<str:prof>/<str:alum>/<str:dia>/<str:lugar>/<str:inicio>/<str:fin>/<str:estado>', views.citaReservadaAceptada , name='reserva'),
    path('asesoria/ver/sinAceptar/<str:prof>/<str:alum>/<str:dia>/<str:lugar>/<str:inicio>/<str:fin>/<str:estado>', views.citaReservadaSinAceptadar , name='reserva'),
    path('asesoria/<str:asesoria>', views.citaReCrear , name='reserva'),
    path('asesoria/cancelar/<str:asesoria>', views.citaCancelar , name='reserva'),
    path('ver/<str:alum>', views.ver , name='ver'),
]
