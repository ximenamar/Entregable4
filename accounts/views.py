from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from main.models import Alumno

class SignUp(generic.CreateView):
    
    form_class = UserCreationForm
    success_url = reverse_lazy('login') #Las vistas genericas no se cargan cuando se importa el archivo
    template_name = 'signup.html'       #se usa reverse_lazy para que se carguen cuando esten disponibles
