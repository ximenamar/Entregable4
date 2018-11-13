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
    aseProf = Asesoria.objects.values('profesor__nombre_profesor').filter(alumno__nombre_alumno = usu).distinct().exclude(estado="Cancelada")
    aseDia = Asesoria.objects.values('dia').filter(alumno__nombre_alumno = usu).exclude(estado="Cancelada")
    print(aseProf)
    nombre = ""
    profCita = ""
    profesor = Cita_Simple.objects.values('profesor__nombre_profesor').filter(profesor__nombre_profesor= profe)
    cant = Cita_Simple.objects.values('profesor__nombre_profesor').filter(profesor__nombre_profesor= profe).exclude(profesor__nombre_profesor__in= aseProf,dia__in=aseDia).count()
    if cant == 0:
        nombre = ["No existe ningún horario disponible del profesor "+profe +" con los filtros de curso: "+ cur+ " y carrera: " + car+"."]
    print(cant)
    a = [""]
    selImp= []
    for i in a:
        selImp.append(profe)

    for a in profesor:
        profCita = Cita_Simple.objects.values('profesor__nombre_profesor','dia', 'lugar','hora_inicio', 'hora_fin').filter(profesor__nombre_profesor = a['profesor__nombre_profesor']).order_by('dia').exclude(profesor__nombre_profesor__in= aseProf,dia__in=aseDia)

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
    print(aseProf)
    print(aseDia)
    nombre = []
    imp = []
    cant = Cita_Simple.objects.values('profesor__nombre_profesor').filter(profesor__nombre_profesor__in= profesor).exclude(profesor__nombre_profesor__in= aseProf,dia__in=aseDia).count()
    print(cant)
    imprimir= [""]
    for a in profesor:
        profCita = Cita_Simple.objects.values('profesor__nombre_profesor','dia', 'lugar','hora_inicio', 'hora_fin').filter(profesor__nombre_profesor = a['profesor__nombre_profesor']).order_by('dia').exclude(profesor__nombre_profesor__in= aseProf,dia__in=aseDia)
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
    print(alumnoCreado)
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

def citaReservadaCancel(request, prof, alum, dia, lugar, inicio, fin, estado):
    '''CREA ALUMNO'''
    alumno = Alumno.objects.values('nombre_alumno').filter(nombre_alumno = alum).distinct()
    alumnoCreado = ""
    for a in alumno:
        alumnoCreado= a["nombre_alumno"]
    print(alumnoCreado)
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

def citaReservadaAceptada(request, prof, alum, dia, lugar, inicio, fin, estado):
    asesoria = Asesoria.objects.values('asesoria','profesor__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado').filter(asesoria = prof+alum+dia).distinct()
    contexto = {
       "asesoria_sel": asesoria,
    }
    return render(request, "asesoriaAceptada.html", contexto)

def citaReservadaSinAceptadar(request, prof, alum, dia, lugar, inicio, fin, estado):
    asesoria = Asesoria.objects.values('asesoria','profesor__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado').filter(asesoria = prof+alum+dia).distinct()
    contexto = {
       "asesoria_sel": asesoria,
    }
    return render(request, "asesoriaAceptada.html", contexto)

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

#Inicio Funciones Profesor
def verProf(request, prof):
     imprimir = ""
     asesoria = Asesoria.objects.values('profesor__nombre_profesor','alumno__nombre_alumno','dia','lugar','hora_inicio','hora_fin','razon','estado').filter(profesor__nombre_profesor = prof ).order_by('estado','dia').exclude(estado = "Cancelada")
     cant =  Asesoria.objects.values('profesor__nombre_profesor').filter(profesor__nombre_profesor = prof).exclude(estado = "Cancelada").count()
     print(cant)
     if cant == 0:
         imprimir = ["Profesor "+prof+", no tienes ninguna asesoría para gestionar"]
     contexto = {
        "lista_asesorias": asesoria,
        "noAse": imprimir
     }
     return render(request, "verAsesoriaProf.html", contexto)

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
    print(profesor)
    print(profesorConsultado)
    contexto = {
        "lista_profesores": profesorConsultado
    }
    return render(request, "crearAse.html", contexto)

def crearCita_simple(request, prof, inicio, fin, dia, lugar, cod):
    profesorAse = Profesor.objects.only('nombre_profesor').filter(nombre_profesor = prof).get()
    cita = Cita_Simple.objects.values('codigo_simple').filter(codigo_simple = cod).distinct()
    cant = Cita_Simple.objects.values('profesor__nombre_profesor').filter(profesor__nombre_profesor = prof ,dia = dia).count()
    print(cant)
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
