from django.test import TestCase
from academico.models import Asignatura, Grado, Grupo


#Test de Pablo Niño
class AsignaturaModelTest(TestCase):
    def test_crear_asignatura(self):
        asignatura = Asignatura.objects.create(nombre="Matemáticas")
        asignatura_recuperada = Asignatura.objects.get(id_asignatura=asignatura.id_asignatura)
        self.assertEqual(asignatura_recuperada.nombre, "Matemáticas")


#test de Victor Cañon
class GradoModelTest(TestCase):
    def test_crear_grado(self):
        grado = Grado.objects.create(nombre="Primero")
        grado_recuperado = Grado.objects.get(id_grado=grado.id_grado)
        self.assertEqual(grado_recuperado.nombre, "Primero")


#Test de Jacobo Alzate
class GrupoModelTest(TestCase):
    def test_crear_grupo(self):
        grado = Grado.objects.create(nombre="Primero")  
        grupo = Grupo.objects.create(nombre="Grupo A", id_grado=grado)  
        grupo_recuperado = Grupo.objects.get(id_grupo=grupo.id_grupo)
        self.assertEqual(grupo_recuperado.nombre, "Grupo A")
        self.assertEqual(grupo_recuperado.id_grado, grado)  


#Test de Jeisson Bareño
class AsignaturaStrTest(TestCase):
    def test_str_asignatura(self):
        asignatura = Asignatura.objects.create(nombre="Física")
        self.assertEqual(str(asignatura), "Física")
