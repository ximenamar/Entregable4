import psycopg2
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import generic
from django.template import loader
from collections import deque
from .models import Carrera, Curso, Profesor, Cita_Simple, Etiqueta, Asesoria

#Inicio de Funciones
def princ(request):
    return render(request, 'principal.html')

def busqueda1(request):
     carreras = Carrera.objects.order_by('nombre_carrera')
     contexto = {
        "lista_carreras": carreras
     }
     return render(request, "busqueda1.html", contexto)

def busqueda1_Cu(request, ca, prof):
     profesor = Profesor.objects.filter(nombre_profesor = prof)
     carreras = Carrera.objects.order_by('nombre_carrera').exclude(nombre_carrera = ca)
     carrera = Carrera.objects.filter(nombre_carrera = ca)
     curso = Curso.objects.filter(carrera__nombre_carrera = ca)
     contexto = {
        "lista_carreras": carreras,
        "lista_cursos": curso,
        "carrera_sel": carrera,
        "profesor_sel": profesor,
     }
     return render(request, "busqueda1f.html", contexto)


def busqueda1_real(request, car, profe, cur):

    profesor = Cita_Simple.objects.values('profesor__nombre_profesor').filter(profesor__nombre_profesor= profe)
    print(profesor)
    nombre = []
    for a in profesor:
        profCita = Cita_Simple.objects.values('profesor__nombre_profesor','dia', 'lugar','hora_inicio', 'hora_fin').filter(profesor__nombre_profesor = a['profesor__nombre_profesor'])
        nombre.append({'profesor' : profCita})
    #print(nombre)
    if profesor != None:
        contexto = {
            "profesor_sel": profCita,
        }
        return render(request, "reservarcita.html", contexto)
    else:
        return render(request, "reservarcita.html")

def busq2(request):
    etiquetas = Etiqueta.objects.values('nombre_etiqueta').distinct()
    contexto = {
       "lista_etiquetas": etiquetas
    }
    return render(request, 'busqueda2.html', contexto)


def busqueda2_real(request, etiq):
    etiquetas = Etiqueta.objects.values('nombre_etiqueta').filter(nombre_etiqueta = etiq).distinct()
    profesor = Etiqueta.objects.values('profesor__nombre_profesor').filter(nombre_etiqueta = etiq)
    nombre = []
    for a in profesor:
        profCita = Cita_Simple.objects.values('profesor__nombre_profesor','dia', 'lugar','hora_inicio', 'hora_fin').filter(profesor__nombre_profesor = a['profesor__nombre_profesor'])
        nombre.append({'profesor' : profCita})
    print(nombre)
    contexto = {
       "profesor_sel": nombre,
    }
    return render(request, "reservarcitaFil.html", contexto)

def citaReservada(request, prof, dia, lugar, inicio, fin):

    conn = psycopg2.connect("host=localhost dbname=mydatabase user=postgres")
    cur = conn.cursor()
    cur.execute("INSERT INTO Asesoria VALUES (%s, %s, %s, %s)", (prof, dia, lugar, inicio, fin))
    conn.commit()



    seleccion = {prof, dia, lugar, inicio, fin}
    asesoria = []
    print(asesoria)
    for a in seleccion:
        asesoria.append({'profesor' : prof })
    print(seleccion)
    contexto = {
       "asesoria_sel": asesoria,
    }
    return render(request, "asesoria.html", contexto)
