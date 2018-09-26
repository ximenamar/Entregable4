from django.db import models

# Create your models here.
class Carrera(models.Model):
    nombre_carrera = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_carrera


class Curso(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    nombre_curso = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_curso


class Profesor(models.Model):
    nombre_profesor = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_profesor
