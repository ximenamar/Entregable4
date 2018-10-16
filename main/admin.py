from django.contrib import admin

from .models import Profesor, Alumno, Seccion, Horario, Asesoria_simple, Asesoria_multiple, Cita, Etiqueta, Semestre, Carrera, Facultad, Curso

admin.site.register(Profesor)

admin.site.register(Alumno)

admin.site.register(Seccion)

admin.site.register(Horario)

admin.site.register(Asesoria_simple)

admin.site.register(Asesoria_multiple)

admin.site.register(Cita)

admin.site.register(Etiqueta)

admin.site.register(Semestre)

admin.site.register(Carrera)

admin.site.register(Facultad)

admin.site.register(Curso)
