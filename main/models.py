from django.db import models
from datetime import datetime
class Administrador(models.Model):
    nombre_administrador = models.CharField(max_length=200, default='Profesor')
    def __str__(self):
        return self.nombre_administrador

class Profesor(models.Model):
    nombre_profesor = models.CharField(max_length=200, default='Profesor')
    def __str__(self):
        return self.nombre_profesor

class Alumno(models.Model):
    nombre_alumno = models.CharField(max_length=200, default='Alumno')
    def __str__(self):
        return self.nombre_alumno

class Cita_Simple(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    codigo_simple = models.CharField(max_length=200, default='Cita')
    hora_inicio = models.CharField(max_length=200)
    hora_fin = models.CharField(max_length=200)
    dia = models.CharField(max_length=200)
    lugar = models.CharField(max_length=200)
    def __str__(self):
        return self.codigo_simple

class Asesoria_Multiple(models.Model):
    asesoria = models.CharField(max_length=200, default='AsesoriaM')
    profesor_uno = models.ForeignKey(Profesor, related_name='profesor_uno' ,on_delete=models.CASCADE)
    profesor_dos = models.ForeignKey(Profesor, related_name='profesor_dos' ,on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    hora_inicio = models.CharField(max_length=200)
    hora_fin = models.CharField(max_length=200)
    dia = models.CharField(max_length=200)
    razon = models.CharField(max_length=200)
    lugar = models.CharField(max_length=200)
    estado = models. CharField(max_length=200, null=True)
    estado2 = models. CharField(max_length=200, null=True)
    mensaje = models. CharField(max_length=200, null=True)
    estado3 = models. CharField(max_length=200, null=True)
    def __str__(self):
        return self.asesoria

class Etiqueta(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    nombre_etiqueta = models.CharField(max_length=200, default='Etiqueta')
    def __str__(self):
        return self.nombre_etiqueta

class Carrera(models.Model):
    nombre_carrera = models.CharField(max_length=200, default='Carrera')
    def __str__(self):
        return self.nombre_carrera

class Curso(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    nombre_curso = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.nombre_curso

class Asesoria(models.Model):
    asesoria = models.CharField(max_length=200, default='Asesoria')
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    dia = models.CharField(max_length=200, null=True)
    lugar= models.CharField(max_length=200, null=True)
    hora_inicio = models.CharField(max_length=200)
    hora_fin = models.CharField(max_length=200)
    razon = models.CharField(max_length=200, null=True)
    estado = models. CharField(max_length=200, null=True)
    def __str__(self):
        return self.asesoria

class Historial(models.Model):
    historial = models.CharField(max_length=200, default='Asesoria')
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    dia = models.CharField(max_length=200, null=True)
    lugar= models.CharField(max_length=200, null=True)
    hora_inicio = models.CharField(max_length=200)
    hora_fin = models.CharField(max_length=200)
    razon = models.CharField(max_length=200, null=True)
    fecha = models.DateTimeField(default=datetime.now, editable=False)
    read_only = 'fecha'
    def __str__(self):
        return self.historial
