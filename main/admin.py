from django.contrib import admin

from .models import Carrera, Curso, Profesor

admin.site.register(Carrera)

admin.site.register(Curso)

admin.site.register(Profesor)
