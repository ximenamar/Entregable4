from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from main.models import Alumno
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages

# class SignUp(generic.CreateView):
#
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login') #Las vistas genericas no se cargan cuando se importa el archivo
#     template_name = 'signup.html'       #se usa reverse_lazy para que se carguen cuando esten disponibles


def registro(request):
    return render(request, "signup.html")


def registrarse(request):
    usuario=request.POST['usuario']
    nombre=request.POST['nombre']
    contra=request.POST['contra']
    tipo=request.POST['tipo']



    if nombre == "" or usuario == "" or contra == "" or tipo == "":
        messages.info(request, "Completa todos los campos")
        return render(request, 'signup.html')
    else:
        user = User.objects.create(
                username=usuario,
                first_name=nombre,
                last_name=tipo,
                password=make_password(contra))
        user.save()
        return render(request, 'home.html')
