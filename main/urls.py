from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.princ , name='principal'),
    path('busqueda1/', views.Busq1.as_view() , name='busqueda1'),
    path('busqueda2/', views.busq2 , name='busqueda2'),
]
