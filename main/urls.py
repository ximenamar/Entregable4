from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.princ , name='principal'),
    path('busqueda1/', views.busqueda1 , name='busqueda1'),
    path('busqueda1/<str:ca>/<str:prof>', views.busqueda1_Cu , name='busqueda1_Cu'),
    path('buscar1/<str:car>/<str:profe>/<str:cur>', views.busqueda1_real , name='buscar1'),
    path('busqueda2/', views.busq2 , name='busqueda2'),
    path('busqueda2/<str:etiq>', views.busqueda2_real , name='busqueda2'),
    path('asesoria/<str:prof>/<str:dia>/<str:lugar>/<str:inicio>/<str:fin>', views.citaReservada , name='reserva'),
]
