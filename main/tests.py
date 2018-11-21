from django.test import TestCase

# Create your tests here.

from main.models import Alumno
from main.models import Administrador
from main.models import Profesor
from main.models import Carrera
from main.models import Etiqueta




class AlumnoModelTest(TestCase):


    def setUp(self):
        Alumno.objects.create(nombre_alumno='Joaquin Mendoza')

    def test_nombre_label(self):
        alumno = Alumno.objects.get(id=1)
        field_label = alumno._meta.get_field('nombre_alumno').verbose_name
        self.assertEquals(field_label,'nombre alumno')

    def test_nombre_max_length(self):
        alumno = Alumno.objects.get(id=1)
        max_length = alumno._meta.get_field('nombre_alumno').max_length
        self.assertEquals(max_length,200)

class AdministradorModelTest(TestCase):

    def setUp(self):
        Administrador.objects.create(nombre_administrador='Hernan Quintana')

    def test_nombre_label(self):
        administrador = Administrador.objects.get(id=1)
        field_label = administrador._meta.get_field('nombre_administrador').verbose_name
        self.assertEquals(field_label,'nombre administrador')

    def test_nombre_max_length(self):
        administrador = Administrador.objects.get(id=1)
        max_length = administrador._meta.get_field('nombre_administrador').max_length
        self.assertEquals(max_length,200)

class ProfesorModelTest(TestCase):


    def setUp(self):
        Profesor.objects.create(nombre_profesor='Juan Cardenaz')

    def test_nombre_label(self):
        profesor = Profesor.objects.get(id=1)
        field_label = profesor._meta.get_field('nombre_profesor').verbose_name
        self.assertEquals(field_label,'nombre profesor')

    def test_nombre_max_length(self):
        profesor = Profesor.objects.get(id=1)
        max_length = profesor._meta.get_field('nombre_profesor').max_length
        self.assertEquals(max_length,200)

class CarreraModelTest(TestCase):


    def setUp(self):
        Carrera.objects.create(nombre_carrera='Comunicaciones')

    def test_nombre_label(self):
        carrera = Carrera.objects.get(id=1)
        field_label = carrera._meta.get_field('nombre_carrera').verbose_name
        self.assertEquals(field_label,'nombre carrera')

    def test_nombre_max_length(self):
        carrera = Carrera.objects.get(id=1)
        max_length = carrera._meta.get_field('nombre_carrera').max_length
        self.assertEquals(max_length,200)

class EtiquetaModelTest(TestCase):

    def setUp(self):
        Profesor.objects.create(nombre_profesor='Juan Cardenaz')
        prof = Profesor.objects.get(id=1)
        Etiqueta.objects.create(nombre_etiqueta='hola',profesor=prof)

    def test_nombre_label(self):
        etiqueta = Etiqueta.objects.get(id=1)
        field_label = etiqueta._meta.get_field('nombre_etiqueta').verbose_name
        self.assertEquals(field_label,'nombre etiqueta')

    def test_nombre_max_length(self):
        etiqueta = Etiqueta.objects.get(id=1)
        max_length = etiqueta._meta.get_field('nombre_etiqueta').max_length
        self.assertEquals(max_length,200)
