from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import generic
from django.template import loader
from .models import Carrera, Curso

# Create your views here.
# class PrincipalView(generic.DetailView):
#     template_name = 'principal.html'

def princ(request):
    return render(request, 'principal.html')

class Busq1(generic.ListView):
    template_name = 'busqueda1.html'
    context_object_name = 'lista_carreras'
    def get_queryset(self):
        return Carrera.objects.order_by('nombre_carrera')


def busq2(request):
    return render(request, 'busqueda2.html')
