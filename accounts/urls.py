from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('signup/', views.registro , name='signup'),
    path('registrarse/', views.registrarse , name='registrar'),
]
