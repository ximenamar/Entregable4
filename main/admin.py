from django.contrib import admin

from .models import *

admin.site.register(Profesor)

admin.site.register(Alumno)

admin.site.register(Cita_Simple)

admin.site.register(Cita_Multiple)

admin.site.register(Etiqueta)

admin.site.register(Carrera)

admin.site.register(Curso)

admin.site.register(Asesoria)
