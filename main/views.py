import psycopg2
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import generic
from django.template import loader
from collections import deque
from .models import *
import pusher
#Notificaciones

def noti(request):
    return render(request, "a.html")

def swal(request):
    pusher_client = pusher.Pusher(
      app_id='641815',
      key='088d8d55c84743f48c36',
      secret='86e8e73a4178e10bc7a9',
      cluster='us2',
      ssl=True
    )

    pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
#Inicio de Funciones Alumno
def princ(request):
    return render(request, 'principal.html')

def ver(request, alum):
     imprimir = ""
     asesoria = Asesoria.objects.values('profesor__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','estado').filter(alumno__nombre_alumno = alum ).order_by('estado','dia')
     cant =  Asesoria.objects.values('profesor__nombre_profesor').filter(alumno__nombre_alumno = alum).count()
     if cant == 0:
         imprimir = [alum+", no has reservado ninguna asesoría"]
     contexto = {
        "lista_asesorias": asesoria,
        "noAse": imprimir
     }
     #Para actualizar las vistas
     pusher_client = pusher.Pusher(
     app_id='642894',
     key='83777adac1c4e636cd80',
     secret='6f59983b4b6fb9481554',
     cluster='us2',
     ssl=True
     )
     pusher_client.trigger('my-channel', 'my-event','aceptada')
     return render(request, "verAsesoria.html", contexto)

def verM(request, alum):
     imprimir = ""
     asesoria = Asesoria_Multiple.objects.values('profesor_uno__nombre_profesor','profesor_dos__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','estado').filter(alumno__nombre_alumno = alum ).order_by('estado','dia')
     cant =  Asesoria_Multiple.objects.values('profesor_uno__nombre_profesor').filter(alumno__nombre_alumno = alum).count()

     if cant == 0:
         imprimir = [alum+", no has reservado ninguna asesoría"]
     contexto = {
        "lista_asesorias": asesoria,
        "noAse": imprimir
     }
     #Para actualizar las vistas
     pusher_client = pusher.Pusher(
     app_id='642894',
     key='83777adac1c4e636cd80',
     secret='6f59983b4b6fb9481554',
     cluster='us2',
     ssl=True
     )
     pusher_client.trigger('my-channel', 'my-event','aceptada')
     return render(request, "verAsesoriaM.html", contexto)

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


def busqueda1_real(request, car, profe, cur, usu):
    aseProfM1 = Asesoria_Multiple.objects.values('profesor_uno__nombre_profesor').filter(alumno__nombre_alumno = usu).distinct().exclude(estado="Cancelada")
    aseProfM2 = Asesoria_Multiple.objects.values('profesor_dos__nombre_profesor').filter(alumno__nombre_alumno = usu).distinct().exclude(estado="Cancelada")
    aseDiaM = Asesoria_Multiple.objects.values('dia').filter(alumno__nombre_alumno = usu).exclude(estado="Cancelada")
    aseProf = Asesoria.objects.values('profesor__nombre_profesor').filter(alumno__nombre_alumno = usu).distinct().exclude(estado="Cancelada")
    aseDia = Asesoria.objects.values('dia').filter(alumno__nombre_alumno = usu).exclude(estado="Cancelada")

    nombre = ""
    profCita = ""
    profesor = Cita_Simple.objects.values('profesor__nombre_profesor').filter(profesor__nombre_profesor= profe)
    cant = Cita_Simple.objects.values('profesor__nombre_profesor').filter(profesor__nombre_profesor= profe).exclude(profesor__nombre_profesor__in= aseProf,dia__in=aseDia).count()
    if cant == 0:
        nombre = ["No existe ningún horario disponible del profesor "+profe +" con los filtros de curso: "+ cur+ " y carrera: " + car+"."]

    a = [""]
    selImp= []
    for i in a:
        selImp.append(profe)

    for a in profesor:
        profCita = Cita_Simple.objects.values('profesor__nombre_profesor','dia', 'lugar','hora_inicio', 'hora_fin').filter(profesor__nombre_profesor = a['profesor__nombre_profesor']).order_by('dia').exclude(profesor__nombre_profesor__in= aseProf,dia__in=aseDia).exclude(profesor__nombre_profesor__in= aseProfM1,dia__in=aseDiaM).exclude(profesor__nombre_profesor__in= aseProfM2, dia__in=aseDiaM)

    contexto = {
        "profesor_sel": profCita,
        "noExiste": nombre,
        "prof": selImp
    }
    return render(request, "reservarcita.html", contexto)


def busq2(request):
    etiquetas = Etiqueta.objects.values('nombre_etiqueta').distinct().order_by('nombre_etiqueta')
    contexto = {
       "lista_etiquetas": etiquetas
    }
    return render(request, 'busqueda2.html', contexto)


def busqueda2_real(request, etiq, usu):
    etiquetas = Etiqueta.objects.values('nombre_etiqueta').filter(nombre_etiqueta = etiq).distinct()
    profesor = Etiqueta.objects.values('profesor__nombre_profesor').filter(nombre_etiqueta = etiq)
    aseProf = Asesoria.objects.values('profesor__nombre_profesor').filter(alumno__nombre_alumno = usu).distinct().exclude(estado="Cancelada")
    aseDia = Asesoria.objects.values('dia').filter(alumno__nombre_alumno = usu).exclude(estado="Cancelada")
    aseProfM1 = Asesoria_Multiple.objects.values('profesor_uno__nombre_profesor').filter(alumno__nombre_alumno = usu).distinct().exclude(estado="Cancelada")
    aseProfM2 = Asesoria_Multiple.objects.values('profesor_dos__nombre_profesor').filter(alumno__nombre_alumno = usu).distinct().exclude(estado="Cancelada")
    aseDiaM = Asesoria_Multiple.objects.values('dia').filter(alumno__nombre_alumno = usu).exclude(estado="Cancelada")

    nombre = []
    imp = []
    cant = Cita_Simple.objects.values('profesor__nombre_profesor').filter(profesor__nombre_profesor__in= profesor).exclude(profesor__nombre_profesor__in= aseProf,dia__in=aseDia).count()

    imprimir= [""]
    for a in profesor:
        profCita = Cita_Simple.objects.values('profesor__nombre_profesor','dia', 'lugar','hora_inicio', 'hora_fin').filter(profesor__nombre_profesor = a['profesor__nombre_profesor']).order_by('dia').exclude(profesor__nombre_profesor__in= aseProf,dia__in=aseDia).exclude(profesor__nombre_profesor__in= aseProfM1,dia__in=aseDiaM).exclude(profesor__nombre_profesor__in= aseProfM2, dia__in=aseDiaM)
        nombre.append({'profesor' : profCita})

    for a in imprimir:
        imp.append(etiq.capitalize())

    if cant == 0:
        imprimir = ["No existen horarios disponibles de los profesores con etiqueta "+etiq]

    contexto = {
       "profesor_sel": nombre,
       "etiq_sel": imp,
       "noExiste": imprimir
    }
    return render(request, "reservarcitaFil.html", contexto)

def citaReservada(request, prof, alum, dia, lugar, inicio, fin):
    '''CREA ALUMNO'''
    alumno = Alumno.objects.values('nombre_alumno').filter(nombre_alumno = alum).distinct()
    alumnoCreado = ""
    for a in alumno:
        alumnoCreado= a["nombre_alumno"]

    if alum != alumnoCreado:
        al = Alumno(nombre_alumno=alum);
        al.save();
    '''CREA CITA'''

    alumnoAse = Alumno.objects.only('nombre_alumno').filter(nombre_alumno = alum).get()
    profesorAse = Profesor.objects.only('nombre_profesor').filter(nombre_profesor = prof).get()
    asesoria = Asesoria.objects.values('asesoria').filter(asesoria = prof+alum+dia).distinct()
    asesoriaCreada = ""

    for i in asesoria:
        asesoriaCreada= i["asesoria"]

    if asesoriaCreada != prof+alum+dia:
        p = Asesoria(asesoria=prof+alum+dia,profesor=profesorAse,alumno=alumnoAse,dia=dia,lugar=lugar,hora_inicio=inicio,hora_fin=fin,razon="Tesis",estado="pendiente a aceptar")
        p.save()
    else:
        Asesoria.objects.filter(asesoria=prof+alum+dia).update(estado = "pendiente a aceptar")
    '''Mostrar Asesoria Creada'''
    seleccion = {prof, dia, lugar, inicio, fin}
    asesoriaDatos = Asesoria.objects.values('asesoria','profesor__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado').filter(asesoria = prof+alum+dia).distinct()
    contexto = {
       "asesoria_sel": asesoriaDatos,
    }
    #actualiza vista profesor
    ase= Asesoria.objects.values('asesoria','profesor__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado').filter(asesoria = prof+alum+dia).get()
    pusher_client = pusher.Pusher(
    app_id='642931',
    key='2294181343cebed3aeea',
    secret='52ba0b81bfd139a56c20',
    cluster='us2',
    ssl=True
    )

    pusher_client.trigger('my-channel', 'my-event',ase)
    #Manda Notificaciones al profesore
    pusher_client = pusher.Pusher(
    app_id='642947',
    key='25d751d0250a1bbbf28b',
    secret='d3ae50e6f9ee8c211be0',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    return render(request, "asesoria.html", contexto)

def citaReservadaMul(request, prof1, prof2, alum, dia, inicio, fin, lugar, razon):
    '''CREA ALUMNO'''
    alumno = Alumno.objects.values('nombre_alumno').filter(nombre_alumno = alum).distinct()
    alumnoCreado = ""
    for a in alumno:
        alumnoCreado= a["nombre_alumno"]

    if alum != alumnoCreado:
        al = Alumno(nombre_alumno=alum);
        al.save();
    '''CREA Asesoria multiple'''

    alumnoAse = Alumno.objects.only('nombre_alumno').filter(nombre_alumno = alum).get()
    profesor_uno = Profesor.objects.only('nombre_profesor').filter(nombre_profesor = prof1).get()
    profesor_dos = Profesor.objects.only('nombre_profesor').filter(nombre_profesor = prof2).get()
    asesoria = Asesoria_Multiple.objects.values('asesoria').filter(asesoria = prof1+prof2+alum+dia).distinct()
    asesoriaCreada = ""

    for i in asesoria:
        asesoriaCreada= i["asesoria"]

    if asesoriaCreada != prof1+prof2+alum+dia:
        p = Asesoria_Multiple(asesoria=prof1+prof2+alum+dia,profesor_uno=profesor_uno,profesor_dos=profesor_dos,alumno=alumnoAse,hora_inicio=inicio,hora_fin=fin,dia=dia,razon=razon,lugar=lugar,estado="pendiente a aceptar",estado2="nada",mensaje="pendiente a aceptar",estado3="nada")
        p.save()
    else:
        Asesoria_Multiple.objects.filter(asesoria=prof1+prof2+alum+dia).update(estado = "pendiente a aceptar")
    '''Mostrar Asesoria Creada'''
    asesoriaDatos = Asesoria_Multiple.objects.values('asesoria','profesor_uno__nombre_profesor', 'profesor_dos__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado').filter(asesoria = prof1+prof2+alum+dia).distinct()
    contexto = {
       "asesoria_sel": asesoriaDatos,
    }
    #actualiza vista profesor
    ase= Asesoria_Multiple.objects.values('asesoria','profesor_uno__nombre_profesor','profesor_dos__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado','estado2','mensaje').filter(asesoria = prof1+prof2+alum+dia).get()
    pusher_client = pusher.Pusher(
    app_id='652674',
    key='a52822b55fd67e542bd1',
    secret='43084338711857118213',
    cluster='us2',
    ssl=True
    )

    pusher_client.trigger('my-channel', 'my-event',ase)
    #Manda Notificaciones al profesore
    pusher_client = pusher.Pusher(
    app_id='652607',
    key='d8a1808870a3d4007260',
    secret='d18e53973c7d937442c7',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    return render(request, "asesoriaMul.html", contexto)

def citaReservadaCancel(request, prof, alum, dia, lugar, inicio, fin, estado):
    '''CREA ALUMNO'''
    alumno = Alumno.objects.values('nombre_alumno').filter(nombre_alumno = alum).distinct()
    alumnoCreado = ""
    for a in alumno:
        alumnoCreado= a["nombre_alumno"]

    if alum != alumnoCreado:
        al = Alumno(nombre_alumno=alum);
        al.save();
    '''CREA CITA'''

    alumnoAse = Alumno.objects.only('nombre_alumno').filter(nombre_alumno = alum).get()
    profesorAse = Profesor.objects.only('nombre_profesor').filter(nombre_profesor = prof).get()
    asesoria = Asesoria.objects.values('asesoria').filter(asesoria = prof+alum+dia).distinct()
    asesoriaCreada = ""

    for i in asesoria:
        asesoriaCreada= i["asesoria"]

    if asesoriaCreada != prof+alum+dia:
        p = Asesoria(asesoria=prof+alum+dia,profesor=profesorAse,alumno=alumnoAse,dia=dia,lugar=lugar,hora_inicio=inicio,hora_fin=fin,razon="Tesis",estado="pendiente a aceptar")
        p.save()

    '''Mostrar Asesoria Creada'''
    seleccion = {prof, dia, lugar, inicio, fin}
    asesoriaDatos = Asesoria.objects.values('asesoria','profesor__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado').filter(asesoria = prof+alum+dia).distinct()
    contexto = {
       "asesoria_sel": asesoriaDatos,
    }
    return render(request, "asesoriaCancel.html", contexto)

def citaReservadaCancelMul(request, ase, prof):
    asesoriaDatos = Asesoria_Multiple.objects.values('asesoria','profesor_uno__nombre_profesor','profesor_dos__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado').filter(asesoria = ase).distinct()
    contexto = {
       "asesoria_sel": asesoriaDatos,
    }
    return render(request, "asesoriaCancelMul.html", contexto)

def citaReservadaAceptada(request, prof, alum, dia, lugar, inicio, fin, estado):
    asesoria = Asesoria.objects.values('asesoria','profesor__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado').filter(asesoria = prof+alum+dia).distinct()
    contexto = {
       "asesoria_sel": asesoria,
    }
    return render(request, "asesoriaAceptada.html", contexto)

def citaReservadaAceptadaMul(request, prof1, prof2, alum, dia, lugar, inicio, fin, estado):
    asesoria = Asesoria_Multiple.objects.values('asesoria','profesor_uno__nombre_profesor','profesor_dos__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado').filter(asesoria = prof1+prof2+alum+dia).distinct()
    contexto = {
       "asesoria_sel": asesoria,
    }
    return render(request, "asesoriaAceptadaMul.html", contexto)

def citaReservadaSinAceptadar(request, prof, alum, dia, lugar, inicio, fin, estado):
    asesoria = Asesoria.objects.values('asesoria','profesor__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado').filter(asesoria = prof+alum+dia).distinct()
    contexto = {
       "asesoria_sel": asesoria,
    }
    return render(request, "asesoriaAceptada.html", contexto)

def citaReservadaSinAceptadarMul(request, prof1, prof2, alum, dia, lugar, inicio, fin, estado):
    asesoria = Asesoria_Multiple.objects.values('asesoria','profesor_uno__nombre_profesor','profesor_dos__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado').filter(asesoria = prof1+prof2+alum+dia).distinct()
    contexto = {
       "asesoria_sel": asesoria,
    }
    return render(request, "asesoriaAceptadaMul.html", contexto)

def citaReCrear(request, asesoria):
    a = asesoria
    Asesoria.objects.filter(asesoria=a).update(estado = "pendiente a aceptar")
    ase = Asesoria.objects.values('alumno__nombre_alumno','profesor__nombre_profesor','estado','dia','lugar','hora_inicio','hora_fin').filter(asesoria = a).get()
    #Actualiza las vistas Profesor
    pusher_client = pusher.Pusher(
    app_id='642931',
    key='2294181343cebed3aeea',
    secret='52ba0b81bfd139a56c20',
    cluster='us2',
    ssl=True
    )

    pusher_client.trigger('my-channel', 'my-event',ase)
    #Manda Notificaciones al profesor
    pusher_client = pusher.Pusher(
    app_id='642947',
    key='25d751d0250a1bbbf28b',
    secret='d3ae50e6f9ee8c211be0',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)

    return HttpResponse("")

def citaReCrearMul(request, asesoria):
    a = asesoria
    Asesoria_Multiple.objects.filter(asesoria=a).update(estado = "pendiente a aceptar", estado2="nada",mensaje="pendiente a aceptar",estado3="nada")
    ase = Asesoria_Multiple.objects.values('alumno__nombre_alumno','profesor_uno__nombre_profesor','profesor_dos__nombre_profesor','estado','dia','lugar','hora_inicio','hora_fin').filter(asesoria = a).get()
    #Actualiza las vistas Profesor
    pusher_client = pusher.Pusher(
    app_id='652674',
    key='a52822b55fd67e542bd1',
    secret='43084338711857118213',
    cluster='us2',
    ssl=True
    )

    pusher_client.trigger('my-channel', 'my-event',ase)
    #Manda Notificaciones al profesor
    pusher_client = pusher.Pusher(
    app_id='652607',
    key='d8a1808870a3d4007260',
    secret='d18e53973c7d937442c7',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)

    return HttpResponse("")

def citaCancelar(request, asesoria):
    a = asesoria
    ase= Asesoria.objects.values('asesoria','profesor__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado').filter(asesoria = a).get()
    prof = Asesoria.objects.values('profesor__nombre_profesor','alumno__nombre_alumno').filter(asesoria = a).get()

    #actualiza las vistas Porfesor
    pusher_client = pusher.Pusher(
    app_id='642931',
    key='2294181343cebed3aeea',
    secret='52ba0b81bfd139a56c20',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    Asesoria.objects.filter(asesoria=a).delete()
    #actualiza las vistas del detalle del profesor
    pusher_client = pusher.Pusher(
    app_id='643084',
    key='7a7e9159031b98a76d93',
    secret='3d56d18b46833ff92fd0',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)

    #Notifica al profesor
    pusher_client = pusher.Pusher(
    app_id='642947',
    key='25d751d0250a1bbbf28b',
    secret='d3ae50e6f9ee8c211be0',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',{"prof": prof['profesor__nombre_profesor'], "alum": prof['alumno__nombre_alumno'], "estatus":"0"})

    return HttpResponse("")

def citaCancelarMul(request, asesoria):
    ase= Asesoria_Multiple.objects.values('asesoria','profesor_uno__nombre_profesor','profesor_dos__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado').filter(asesoria = asesoria).get()
    prof = Asesoria_Multiple.objects.values('profesor_uno__nombre_profesor','profesor_dos__nombre_profesor','alumno__nombre_alumno').filter(asesoria = asesoria).get()
    print(ase)
    #actualiza las vistas Porfesor
    pusher_client = pusher.Pusher(
    app_id='652674',
    key='a52822b55fd67e542bd1',
    secret='43084338711857118213',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    Asesoria_Multiple.objects.filter(asesoria=asesoria).delete()
    #actualiza las vistas del detalle del profesor
    pusher_client = pusher.Pusher(
    app_id='652692',
    key='bfd2a41b86394aa0eaa4',
    secret='e28f98a072bc83a752dc',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    #Notifica al profesor
    pusher_client = pusher.Pusher(
    app_id='652607',
    key='d8a1808870a3d4007260',
    secret='d18e53973c7d937442c7',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',{"prof1": prof['profesor_uno__nombre_profesor'],"prof2": prof['profesor_dos__nombre_profesor'], "alum": prof['alumno__nombre_alumno'], "estatus":"0"})

    return HttpResponse("")

def busqM(request):
    imprimir = "día"
    selVer = []
    a = [""]
    cita = ""
    noEx = ""
    cita = Cita_Simple.objects.values('dia').order_by('dia').distinct()
    if cita.count()==0:
        cita = ""
        noEx = "No hay días que tengan asesorías disponibles para la selección múltiple de pofesor"
    for i in a:
        selVer.append(imprimir)

    contexto = {
        "lista_citas": cita,
        "filtrado": selVer,
        "no": noEx
     }
    return render(request, "verDiaAsesoriaM.html", contexto)

def verHoraM(request, dia):
    imprimir = "Horario"
    selVer = []
    selDia = []
    a = [""]
    cita = ""
    noEx = []
    cita = Cita_Simple.objects.values('hora_inicio', 'hora_fin').filter(dia = dia).distinct()[::-1]
    cant = Cita_Simple.objects.values('hora_inicio', 'hora_fin').filter(dia = dia).distinct()
    if cant.count()==0:
        cita = ""
        mensaje = "No hay horarios que tengan asesorías disponibles para la selección múltiple de pofesor"
        for i in a:
            noEx.append(mensaje)
    for i in a:
        selVer.append(imprimir)

    for i in a:
        selDia.append(dia)

    contexto = {
        "lista_citas": cita,
        "filtrado": selVer,
        "no": noEx,
        "dia": selDia
     }
    return render(request, "verHoraAsesoriaM.html", contexto)

def verAseMult (request, dia, inicio, fin, usu):
    aseProf = Asesoria.objects.values('profesor__nombre_profesor').filter(alumno__nombre_alumno = usu).distinct().exclude(estado="Cancelada")
    aseDia = Asesoria.objects.values('dia').filter(alumno__nombre_alumno = usu).exclude(estado="Cancelada")
    aseProfM1 = Asesoria_Multiple.objects.values('profesor_uno__nombre_profesor').filter(alumno__nombre_alumno = usu).distinct().exclude(estado="Cancelada")
    aseProfM2 = Asesoria_Multiple.objects.values('profesor_dos__nombre_profesor').filter(alumno__nombre_alumno = usu).distinct().exclude(estado="Cancelada")
    aseDiaM = Asesoria_Multiple.objects.values('dia').filter(alumno__nombre_alumno = usu).exclude(estado="Cancelada")
    nombre = []
    a = [""]
    asesoriaMul = ""
    noEx = ""
    selDia = []
    asesoriaMul = Cita_Simple.objects.values('dia','lugar','hora_inicio','hora_fin').filter(dia = dia, hora_inicio = inicio, hora_fin = fin).distinct().exclude(profesor__nombre_profesor__in= aseProf,dia__in=aseDia).exclude(profesor__nombre_profesor__in= aseProfM1,dia__in=aseDiaM).exclude(profesor__nombre_profesor__in= aseProfM2, dia__in=aseDiaM)
    asesoriaMulProf = Cita_Simple.objects.values('profesor__nombre_profesor').filter(dia = dia, hora_inicio = inicio, hora_fin = fin).distinct().exclude(profesor__nombre_profesor__in= aseProf,dia__in=aseDia).exclude(profesor__nombre_profesor__in= aseProfM1,dia__in=aseDiaM).exclude(profesor__nombre_profesor__in= aseProfM2, dia__in=aseDiaM)

    if asesoriaMulProf.count()<=1:
        asesoriaMul = ""
        asesoriaMulProf = ""
        noEx = "No hay horarios que tengan asesorías disponibles para la selección múltiple de pofesor"
        for i in a:
            nombre.append(noEx)
    for i in a:
        selDia.append(dia)
    contexto = {
       "asesoriasM": asesoriaMul,
       "profesor": asesoriaMulProf,
       "noExiste": nombre,
       "dia": selDia
    }
    return render(request, "reservarcitaMul.html", contexto)

#Inicio Funciones Profesor
def verProf(request, prof):
     imprimir = ""
     asesoria = Asesoria.objects.values('profesor__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado').filter(profesor__nombre_profesor = prof ).order_by('estado','dia').exclude(estado = "Cancelada")
     cant =  Asesoria.objects.values('profesor__nombre_profesor').filter(profesor__nombre_profesor = prof).exclude(estado = "Cancelada").count()

     if cant == 0:
         imprimir = ["Profesor "+prof+", no tienes ninguna asesoría para gestionar"]
     contexto = {
        "lista_asesorias": asesoria,
        "noAse": imprimir
     }
     return render(request, "verAsesoriaProf.html", contexto)

def verProfMul(request, prof):
     imprimir = ""
     prof1 = Asesoria_Multiple.objects.values('profesor_uno__nombre_profesor').filter(profesor_uno__nombre_profesor = prof ).exclude(estado = "Cancelada")
     prof2 = Asesoria_Multiple.objects.values('profesor_dos__nombre_profesor').filter(profesor_dos__nombre_profesor = prof ).exclude(estado = "Cancelada")
     cant = 0
     asesoria = ""
     if prof1.count() == 1:
         asesoria = Asesoria_Multiple.objects.values('profesor_uno__nombre_profesor','profesor_dos__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado','mensaje').filter(profesor_uno__nombre_profesor = prof ).order_by('estado','dia').exclude(estado = "Cancelada")
         cant =  Asesoria_Multiple.objects.values('profesor_uno__nombre_profesor','profesor_dos__nombre_profesor').filter(profesor_uno__nombre_profesor = prof).exclude(estado = "Cancelada").count()
     if prof2.count() == 1:
        asesoria = Asesoria_Multiple.objects.values('profesor_uno__nombre_profesor','profesor_dos__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado','mensaje').filter(profesor_dos__nombre_profesor = prof ).order_by('estado','dia').exclude(estado = "Cancelada")
        cant =  Asesoria_Multiple.objects.values('profesor_uno__nombre_profesor','profesor_dos__nombre_profesor').filter(profesor_dos__nombre_profesor = prof).exclude(estado = "Cancelada").count()

     if cant == 0:
         imprimir = ["Profesor "+prof+", no tienes ninguna asesoría múltiple para gestionar"]
     contexto = {
        "lista_asesorias": asesoria,
        "noAse": imprimir
     }
     return render(request, "verAsesoriaProfMul.html", contexto)

def citaReservadaProf(request, prof, alum, dia, lugar, inicio, fin):
    '''CREA CITA'''

    alumnoAse = Alumno.objects.only('nombre_alumno').filter(nombre_alumno = alum).get()
    profesorAse = Profesor.objects.only('nombre_profesor').filter(nombre_profesor = prof).get()
    asesoria = Asesoria.objects.values('asesoria').filter(asesoria = prof+alum+dia).distinct()
    asesoriaCreada = ""

    for i in asesoria:
        asesoriaCreada= i["asesoria"]

    if asesoriaCreada != prof+alum+dia:
        p = Asesoria(asesoria=prof+alum+dia,profesor=profesorAse,alumno=alumnoAse,dia=dia,lugar=lugar,hora_inicio=inicio,hora_fin=fin,razon="Tesis",estado="pendiente a aceptar")
        p.save()

    '''Mostrar Asesoria Creada'''
    seleccion = {prof, dia, lugar, inicio, fin}
    asesoriaDatos = Asesoria.objects.values('asesoria','profesor__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado').filter(asesoria = prof+alum+dia).distinct()
    contexto = {
       "asesoria_sel": asesoriaDatos,
    }
    return render(request, "asesoriaProf.html", contexto)

def citaReservadaProfMul(request, prof1, prof2, alum, dia, lugar, inicio, fin, razon):

    asesoriaDatos = Asesoria_Multiple.objects.values('asesoria','profesor_uno__nombre_profesor','profesor_dos__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado','mensaje','estado2').filter(asesoria = prof1+prof2+alum+dia).distinct()
    contexto = {
       "asesoria_sel": asesoriaDatos,
    }
    return render(request, "asesoriaProfMul.html", contexto)


def citaAceptar(request, asesoria):
    a = asesoria
    Asesoria.objects.filter(asesoria=a).update(estado = "aceptada")
    ase = Asesoria.objects.values('alumno__nombre_alumno','profesor__nombre_profesor','estado','dia','lugar','hora_inicio','hora_fin').filter(asesoria = a).get()
    #MNotificaciones al alumno
    pusher_client = pusher.Pusher(
      app_id='641815',
      key='088d8d55c84743f48c36',
      secret='86e8e73a4178e10bc7a9',
      cluster='us2',
      ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event', ase)
    #actualiza la vista alumno
    pusher_client = pusher.Pusher(
    app_id='642894',
    key='83777adac1c4e636cd80',
    secret='6f59983b4b6fb9481554',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    #actualiza la vista de detalles del alumno
    pusher_client = pusher.Pusher(
    app_id='642983',
    key='9022786e650c83d9e11f',
    secret='9deebca47bceb88120d6',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    return HttpResponse("")

def citaAceptarMul(request, asesoria, prof):
    a = asesoria

    estado2 = Asesoria_Multiple.objects.values('estado2').filter(asesoria=a)
    for i in estado2:
        est= i["estado2"]
    if est=="nada":
        Asesoria_Multiple.objects.filter(asesoria=a).update(estado2 = prof, mensaje="aceptada solo por "+prof)
    elif est!=prof:
        Asesoria_Multiple.objects.filter(asesoria=a).update(estado = "aceptada", mensaje="aceptada")
    ase = Asesoria_Multiple.objects.values('alumno__nombre_alumno','profesor_uno__nombre_profesor','profesor_dos__nombre_profesor','estado','estado2','estado3','mensaje','dia','lugar','hora_inicio','hora_fin').filter(asesoria = a).get()
    #MNotificaciones al alumno
    pusher_client = pusher.Pusher(
    app_id='652621',
    key='73e158ad0bb9df83fad2',
    secret='eeedd72bdcac9d8dc6ad',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event', ase)
    #actualiza la vista alumno
    pusher_client = pusher.Pusher(
    app_id='642894',
    key='83777adac1c4e636cd80',
    secret='6f59983b4b6fb9481554',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    #actualiza la vista de detalles del alumno al retroceder
    pusher_client = pusher.Pusher(
    app_id='652652',
    key='f59f14bf549768f82204',
    secret='fe18123531d192684497',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)

    #actualiz la vista de asesorias múltiples cuando de un prof cuando el otro prof acepta
    pusher_client = pusher.Pusher(
    app_id='652674',
    key='a52822b55fd67e542bd1',
    secret='43084338711857118213',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    #retrocede la vista de asesorias multiples del detalle de un prof cuando el otro prof acepta
    pusher_client = pusher.Pusher(
    app_id='652734',
    key='ff9c9365a383f65c66a0',
    secret='9d10d2e05514d603d9b3',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    #Manda una notificacion al otro profesor cuando el profesor acepta la asesoria
    pusher_client = pusher.Pusher(
    app_id='653538',
    key='e6c21365f0ce01bcf6bd',
    secret='d1081b5f5dd4a77cd10b',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    return HttpResponse("")

def citaNoAceptar(request, asesoria):
    a = asesoria
    Asesoria.objects.filter(asesoria=a).update(estado = "Cancelada")
    ase = Asesoria.objects.values('alumno__nombre_alumno','profesor__nombre_profesor','estado','dia','lugar','hora_inicio','hora_fin').filter(asesoria = a).get()
    #Notificaciones al alumno
    pusher_client = pusher.Pusher(
    app_id='641815',
    key='088d8d55c84743f48c36',
    secret='86e8e73a4178e10bc7a9',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event', ase)
    #Actualiza ventana de alumno
    pusher_client = pusher.Pusher(
    app_id='642894',
    key='83777adac1c4e636cd80',
    secret='6f59983b4b6fb9481554',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    #alctualiza ventana abrta al ver detalles para no incumplir con los asesoriaDatos
    pusher_client = pusher.Pusher(
    app_id='642983',
    key='9022786e650c83d9e11f',
    secret='9deebca47bceb88120d6',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    return HttpResponse("")

def citaNoAceptarMul(request, asesoria):
    a = asesoria
    Asesoria_Multiple.objects.filter(asesoria=a).update(estado = "Cancelada")
    ase = Asesoria_Multiple.objects.values('alumno__nombre_alumno','profesor_uno__nombre_profesor', 'profesor_dos__nombre_profesor','estado','estado3','dia','lugar','hora_inicio','hora_fin').filter(asesoria = a).get()
    #Notificaciones al alumno
    pusher_client = pusher.Pusher(
    app_id='652621',
    key='73e158ad0bb9df83fad2',
    secret='eeedd72bdcac9d8dc6ad',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event', ase)
    #Actualiza ventana de alumno
    pusher_client = pusher.Pusher(
    app_id='642894',
    key='83777adac1c4e636cd80',
    secret='6f59983b4b6fb9481554',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    #alctualiza ventana abrta al ver detalles para no incumplir con los asesoriaDatos
    pusher_client = pusher.Pusher(
    app_id='652652',
    key='f59f14bf549768f82204',
    secret='fe18123531d192684497',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    #actualiza la vista de asesorias multiples del profesor cuando el otro no acepte
    pusher_client = pusher.Pusher(
    app_id='652674',
    key='a52822b55fd67e542bd1',
    secret='43084338711857118213',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    #Retrocede al porfesor de la vista de deatalles cuando el otro profesor no acepta la asesoría multiple
    pusher_client = pusher.Pusher(
    app_id='652750',
    key='c5c645f25c3aa7ee58de',
    secret='2b9b1ca4c5308d654c3a',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    #Notifica al profesor que otro profesor no ha aceptado la cita
    pusher_client = pusher.Pusher(
    app_id='653595',
    key='5854bf79ddfcd99309b0',
    secret='2ef774f21201cde990f7',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    return HttpResponse("")

def citaReservadaProfCancel(request, prof, alum, dia, lugar, inicio, fin, estado):
    alumnoAse = Alumno.objects.only('nombre_alumno').filter(nombre_alumno = alum).get()
    profesorAse = Profesor.objects.only('nombre_profesor').filter(nombre_profesor = prof).get()
    asesoria = Asesoria.objects.values('asesoria').filter(asesoria = prof+alum+dia).distinct()
    asesoriaCreada = ""

    for i in asesoria:
        asesoriaCreada= i["asesoria"]

    if asesoriaCreada != prof+alum+dia:
        p = Asesoria(asesoria=prof+alum+dia,profesor=profesorAse,alumno=alumnoAse,dia=dia,lugar=lugar,hora_inicio=inicio,hora_fin=fin,razon="Tesis",estado="pendiente a aceptar")
        p.save()

    '''Mostrar Asesoria Creada'''
    seleccion = {prof, dia, lugar, inicio, fin}
    asesoriaDatos = Asesoria.objects.values('asesoria','profesor__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado').filter(asesoria = prof+alum+dia).distinct()
    contexto = {
       "asesoria_sel": asesoriaDatos,
    }
    return render(request, "asesoriaProfCancel.html", contexto)

def citaReservadaProfCancelMul(request, asesoria):

    asesoriaDatos = Asesoria_Multiple.objects.values('asesoria','profesor_uno__nombre_profesor','profesor_dos__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado','mensaje','estado3').filter(asesoria = asesoria).distinct()
    contexto = {
       "asesoria_sel": asesoriaDatos,
    }
    return render(request, "asesoriaProfCancelMul.html", contexto)

def crearProf(request, prof):
    profesor = Profesor.objects.values('nombre_profesor').filter(nombre_profesor = prof).distinct()
    profesorCreado = ""
    for a in profesor:
        profesorCreado= a["nombre_profesor"]

    if prof != profesorCreado:
        pr = Profesor(nombre_profesor=prof);
        pr.save();

    return HttpResponse("")

def citaAtendida(request, asesoria, prof, alum, dia, lugar, inicio, fin, razon):
    alumnoAse = Alumno.objects.only('nombre_alumno').filter(nombre_alumno = alum).get()
    profesorAse = Profesor.objects.only('nombre_profesor').filter(nombre_profesor = prof).get()
    hist = Historial(historial=asesoria,profesor=profesorAse,alumno=alumnoAse,hora_inicio=inicio,hora_fin=fin,dia=dia,lugar=lugar,razon=razon)
    hist.save()
    a = asesoria
    Asesoria.objects.filter(asesoria=a).update(estado = "marcado")
    ase = Asesoria.objects.values('alumno__nombre_alumno','profesor__nombre_profesor','estado','dia','lugar','hora_inicio','hora_fin').filter(asesoria = a).get()
    #MNotificaciones al alumno
    pusher_client = pusher.Pusher(
      app_id='641815',
      key='088d8d55c84743f48c36',
      secret='86e8e73a4178e10bc7a9',
      cluster='us2',
      ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event', ase)
    Asesoria.objects.filter(asesoria=a).delete()
    #actualiza la vista alumno
    pusher_client = pusher.Pusher(
    app_id='642894',
    key='83777adac1c4e636cd80',
    secret='6f59983b4b6fb9481554',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    #actualiza la vista de detalles del alumno
    pusher_client = pusher.Pusher(
    app_id='642983',
    key='9022786e650c83d9e11f',
    secret='9deebca47bceb88120d6',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)

    return HttpResponse("")

def citaAtendidaMul(request, asesoria, prof, alum, dia, lugar, inicio, fin, razon):
    alumnoAse = Alumno.objects.only('nombre_alumno').filter(nombre_alumno = alum).get()
    profesorAse = Profesor.objects.only('nombre_profesor').filter(nombre_profesor = prof).get()
    hist = Historial(historial=asesoria,profesor=profesorAse,alumno=alumnoAse,hora_inicio=inicio,hora_fin=fin,dia=dia,lugar=lugar,razon=razon)
    hist.save()
    a = asesoria
    estado3 = Asesoria_Multiple.objects.values('estado3').filter(asesoria=a)
    for i in estado3:
        est= i["estado3"]
    if est=="nada":
        Asesoria_Multiple.objects.filter(asesoria=a).update(estado3 = prof)
    elif est!=prof:
        Asesoria_Multiple.objects.filter(asesoria=a).update(estado = "marcado")


    ase = Asesoria_Multiple.objects.values('alumno__nombre_alumno','profesor_uno__nombre_profesor','profesor_dos__nombre_profesor','estado','estado3','mensaje','dia','lugar','hora_inicio','hora_fin').filter(asesoria = a).get()
    #MNotificaciones al alumno
    pusher_client = pusher.Pusher(
    app_id='652621',
    key='73e158ad0bb9df83fad2',
    secret='eeedd72bdcac9d8dc6ad',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event', ase)

    estado3 = Asesoria_Multiple.objects.values('estado3').filter(asesoria=a)
    for i in estado3:
        est= i["estado3"]
    if est != prof :
        Asesoria_Multiple.objects.filter(asesoria=a).delete()
    #actualiza la vista alumno
    pusher_client = pusher.Pusher(
    app_id='642894',
    key='83777adac1c4e636cd80',
    secret='6f59983b4b6fb9481554',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    #actualiza la vista de detalles del alumno alretroceder
    pusher_client = pusher.Pusher(
    app_id='652652',
    key='f59f14bf549768f82204',
    secret='fe18123531d192684497',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    #Actualiza la vista de asesorias multiples de un profesor al marcar el otro como atendido
    pusher_client = pusher.Pusher(
    app_id='652674',
    key='a52822b55fd67e542bd1',
    secret='43084338711857118213',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    #retrocede la vista de detalles de aseosria multiple de un profesor cuando el otro marca como atendido
    pusher_client = pusher.Pusher(
    app_id='653521',
    key='8727adc639d7ffc412bc',
    secret='11eb0e3a331e329e22ab',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    #Notifica al otro profesro q no se olvide marcar como atendido cuando el otro lo marca
    pusher_client = pusher.Pusher(
    app_id='653599',
    key='753b74e98fa54eeb6bb8',
    secret='3c0b79479d32b19b07ff',
    cluster='us2',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',ase)
    return HttpResponse("")


def verHisAse(request, tipo,prof):
    imprimir = "día"
    selVer = []
    a = [""]
    cita = ""
    noEx = ""
    if tipo == "alum":
        cita = Historial.objects.values('alumno__nombre_alumno').filter(profesor__nombre_profesor=prof).order_by('alumno__nombre_alumno').distinct()
        imprimir = "alumno"
    else:
        cita = Historial.objects.values('dia').filter(profesor__nombre_profesor=prof).order_by('dia').distinct()
    if cita.count()==0:
        cita = ""
        noEx = "No exiten registros"
    for i in a:
        selVer.append(imprimir)

    contexto = {
        "lista_citas": cita,
        "filtrado": selVer,
        "no": noEx
     }
    return render(request, "verHistorialAsesoria.html", contexto)

def verHisFil(request, sel):
    citaAlum = Historial.objects.values('alumno__nombre_alumno','razon','hora_inicio','hora_fin','dia','lugar','fecha').filter(alumno__nombre_alumno=sel).order_by('-fecha')
    citaDia = Historial.objects.values('alumno__nombre_alumno','razon','hora_inicio','hora_fin','dia','lugar','fecha').filter(dia=sel).order_by('-fecha')
    noneAlum = citaAlum.count()
    noneDia = citaDia.count()

    selVer = []
    a = [""]
    selImp= []
    imprimir = "alumno"
    for i in a:
        selVer.append(sel)

    if noneAlum != 0 and noneDia==0:
        cita = citaAlum
        imprimir = "día"
    else:
        cita = citaDia

    for i in a:
        selImp.append(imprimir)

    contexto = {
        "lista_citas": cita,
        "seleccion": selVer,
        "filtrado": selImp
    }
    return render(request, "verHistorialTipo.html", contexto)

#Funciones del administrador

def crearAdmin(request, admin):
    administrador = Administrador.objects.values('nombre_administrador').filter(nombre_administrador = admin).distinct()
    adminCreado = ""
    for a in administrador:
        adminCreado= a["nombre_administrador"]
    if admin != adminCreado:
        ad = Administrador(nombre_administrador=admin);
        ad.save();
    return HttpResponse("")

def crearAse(request, admin):
    profesor = Profesor.objects.values('nombre_profesor')
    profesorConsultado = []
    for a in profesor:
        profesorConsultado.append( {"nombre" : a["nombre_profesor"]})

    contexto = {
        "lista_profesores": profesorConsultado
    }
    return render(request, "crearAse.html", contexto)

def crearCita_simple(request, prof, inicio, fin, dia, lugar, cod):
    profesorAse = Profesor.objects.only('nombre_profesor').filter(nombre_profesor = prof).get()
    cita = Cita_Simple.objects.values('codigo_simple').filter(codigo_simple = cod).distinct()
    cant = Cita_Simple.objects.values('profesor__nombre_profesor').filter(profesor__nombre_profesor = prof ,dia = dia).count()

    citaCreada = ""
    resp = ""
    for i in cita:
        citaCreada= i["codigo_simple"]

    if cant != 2:
        if citaCreada != cod:
            c = Cita_Simple(profesor=profesorAse,codigo_simple=cod,hora_inicio=inicio,hora_fin=fin,dia=dia,lugar=lugar)
            c.save()
            resp = "ok"
    else:
        resp=cant
    return HttpResponse(resp)

def verAse(request, tipo):
    imprimir = "día"
    selVer = []
    a = [""]
    if tipo == "prof":
        cita = Cita_Simple.objects.values('profesor__nombre_profesor').distinct().order_by('profesor__nombre_profesor')
        imprimir = "profesor"
    else:
        cita = Cita_Simple.objects.values('dia').distinct().order_by('dia')

    for i in a:
        selVer.append(imprimir)

    contexto = {
        "lista_citas": cita,
        "filtrado": selVer
     }
    return render(request, "verAsesoriaAdmin.html", contexto)

def verAseFil(request, sel):
    citaProf = Cita_Simple.objects.values('profesor__nombre_profesor','codigo_simple','hora_inicio','hora_fin','dia','lugar').filter(profesor__nombre_profesor=sel).order_by('dia')
    citaDia = Cita_Simple.objects.values('profesor__nombre_profesor','codigo_simple','hora_inicio','hora_fin','dia','lugar').filter(dia=sel).order_by('profesor__nombre_profesor')
    noneProf = citaProf.count()
    noneDia = citaDia.count()

    selVer = []
    a = [""]
    selImp= []
    imprimir = "profesor"
    for i in a:
        selVer.append(sel)

    if noneProf != 0 and noneDia==0:
        cita = citaProf
        imprimir = "día"
    else:
        cita = citaDia

    for i in a:
        selImp.append(imprimir)

    contexto = {
        "lista_citas": cita,
        "seleccion": selVer,
        "filtrado": selImp
    }
    return render(request, "verHoraTipo.html", contexto)

def elimiAse(request, cita):
    Cita_Simple.objects.filter(codigo_simple=cita).delete()
    return HttpResponse("")

def modAse(request, cita):
    cita = Cita_Simple.objects.values('profesor__nombre_profesor','codigo_simple','hora_inicio','hora_fin','dia','lugar').filter(codigo_simple=cita)
    contexto = {
        "lista_citas": cita
     }
    return render(request, "modificarAse.html", contexto)

def modCita_simple(request, prof, inicio, fin, dia, lugar, cod, codElimi):
    profesorAse = Profesor.objects.only('nombre_profesor').filter(nombre_profesor = prof).get()
    cita = Cita_Simple.objects.values('codigo_simple').filter(codigo_simple = cod).distinct()
    cant = Cita_Simple.objects.values('profesor__nombre_profesor').filter(profesor__nombre_profesor = prof ,dia = dia).count()
    citaMod = ""
    resp = ""
    for i in cita:
        citaMod= i["codigo_simple"]

    if cant != 2:
        if citaMod != cod:
            c = Cita_Simple(profesor=profesorAse,codigo_simple=cod,hora_inicio=inicio,hora_fin=fin,dia=dia,lugar=lugar)
            c.save()
            Cita_Simple.objects.filter(codigo_simple=codElimi).delete()
            resp = "ok"
    else:
        resp=cant
    return HttpResponse(resp)
