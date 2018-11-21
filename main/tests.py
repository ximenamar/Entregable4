from django.test import TestCase

# Create your tests here.

from main.models import Alumno
from main.models import Administrador
from main.models import Profesor
from main.models import Carrera
from main.models import Curso


class AlumnoModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Alumno.objects.create(nombre_alumno='Joaquin Mendoza')

    def test_nombre_label(self):
        alumno = alumno.objects.get(id=1)
        field_label = alumno._meta.get_field('nombre_alumno').verbose_name
        self.assertEquals(field_label,'nombre_alumno')

    def test_nombre_max_length(self):
        alumno = alumno.object.get(id=1)
        max_length = alumno._meta.get_field('nombre_alumno').max_length
        self.assertEquals(max_length,200)

class AdministradorModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Administrador.objects.create(nombre_administrador='Hernan Quintana')

    def test_nombre_label(self):
        administrador = administrador.objects.get(id=1)
        field_label = administrador._meta.get_field('nombre_administrador').verbose_name
        self.assertEquals(field_label,'nombre_administrador')

    def test_nombre_max_length(self):
        administrador = administrador.object.get(id=1)
        max_length = administrador._meta.get_field('nombre_administrador').max_length
        self.assertEquals(max_length,200)

class ProfesorModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Profesor.objects.create(nombre_profesor='Juan Cardenaz')

    def test_nombre_label(self):
        profesor = profesor.objects.get(id=1)
        field_label = profesor._meta.get_field('nombre_profesor').verbose_name
        self.assertEquals(field_label,'nombre_profesor')

    def test_nombre_max_length(self):
        profesor = profesor.object.get(id=1)
        max_length = profesor._meta.get_field('nombre_profesor').max_length
        self.assertEquals(max_length,200)

class CarreraModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Carrera.objects.create(nombre_carrera='Comunicaciones')

    def test_nombre_label(self):
        carrera = carrera.objects.get(id=1)
        field_label = carrera._meta.get_field('nombre_carrera').verbose_name
        self.assertEquals(field_label,'nombre_carrera')

    def test_nombre_max_length(self):
        carrera = carrera.object.get(id=1)
        max_length = carrera._meta.get_field('nombre_carrera').max_length
        self.assertEquals(max_length,200)

class CursoModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Curso.objects.create(nombre_curso='Software II')

    def test_nombre_label(self):
        curso = curso.objects.get(id=1)
        field_label = curso._meta.get_field('nombre_curso').verbose_name
        self.assertEquals(field_label,'nombre_curso')

    def test_nombre_max_length(self):
        curso = curso.object.get(id=1)
        max_length = curso._meta.get_field('nombre_curso').max_length
        self.assertEquals(max_length,200)
