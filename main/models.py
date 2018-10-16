from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre_profesor = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_profesor

class Alumno(models.Model):
    nombre_alumno = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_alumno

class Seccion(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    numero_seccion = models.CharField(max_length=200)
    def __str__(self):
        return self.numero_seccion

class Horario(object):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    codigo_horario = models.CharField(max_length=200)
    inicio = models.CharField(max_length=200)
    fin = models.CharField(max_length=200)
    def __str__(self):
        return self.codigo_horario

class Asesoria_simple(models.Model):
    codigo_asesoria_simple = models.CharField(max_length=200)
    def __str__(self):
        return self.codigo_asesoria_simple

class Asesoria_multiple(models.Model):
    codigo_asesoria_multiple = models.CharField(max_length=200)
    def __str__(self):
        return self.codigo_asesoria_multiple

class Cita(models.Model):
    asesoria_simple = models.ForeignKey(Asesoria_simple, on_delete=models.CASCADE)
    asesoria_multiple = models.ForeignKey(Asesoria_multiple, on_delete=models.CASCADE)
    codigo_cita = models.CharField(max_length=200)
    fecha = models.CharField(max_length=200)
    razon = models.CharField(max_length=200)
    lugar = models.CharField(max_length=200)
    def __str__(self):
        return self.codigo_cita

class Etiqueta(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    asesoria = models.ForeignKey(Asesoria_simple, on_delete=models.CASCADE)
    nombre_etiqueta = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_etiqueta

class Semestre(models.Model):
    nombre_semestre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_semestre

class Carrera(models.Model):
    nombre_carrera = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_carrera

class Facultad(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    nombre_facultad = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_facultad

class Curso(models.Model):
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    nombre_curso = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_curso

