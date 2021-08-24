from django.test import TestCase

import datetime

from django.test import TestCase

from .models import Estudiante, Profesor, Ciudad, Grupo

from django.core.exceptions import ValidationError 

class EstudianteModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.profe = Profesor(nombre="Pedro")
        cls.profe.save()
        cls.grupo = Grupo(nombre="A1", profesor_guia=cls.profe)
        cls.grupo.save()
        cls.ciudad = Ciudad(nombre="Holguín")
        cls.ciudad.save()

    def test_prueba_que_no_se_guarde_estudiante_con_email_none(self):

        nuevo_estudiante = Estudiante(
            nombre="Alfredito", 
            sexo="M", 
            email=None, 
            ciudad_nacimiento = self.ciudad,
            fecha_nacimiento = datetime.datetime(1977, 12, 6),
            grupo = self.grupo)
        try:
            nuevo_estudiante.full_clean()
        except Exception as e:
            self.assertEqual(e.__str__(), "{'email': ['This field cannot be null.']}")

    def test_prueba_que_no_se_guarde_estudiante_con_email_vacio(self):

        nuevo_estudiante = Estudiante(
            nombre="Alfredito", 
            sexo="M", 
            email='', 
            ciudad_nacimiento = self.ciudad,
            fecha_nacimiento = datetime.datetime(1977, 12, 6),
            grupo = self.grupo)
        try:
            nuevo_estudiante.full_clean()
        except Exception as e:
            self.assertEqual(e.__str__(), "{'email': ['This field cannot be blank.']}")

    def test_prueba_que_no_se_guarde_estudiante_con_email_incorrecto(self):

        nuevo_estudiante = Estudiante(
            nombre="Alfredito", 
            sexo="M", 
            email='emailmalformado', 
            ciudad_nacimiento = self.ciudad,
            fecha_nacimiento = datetime.datetime(1977, 12, 6),
            grupo = self.grupo)
        try:
            nuevo_estudiante.full_clean()
            self.fail()
        except Exception as e:
            self.assertEqual(e.__str__(), "{'email': ['Enter a valid email address.']}")

    def test_prueba_que_no_se_guarde_estudiante_con_fecha_nacimiento_en_el_futuro(self):
        
        date_in_future = datetime.datetime(datetime.datetime.now().year+1, 12, 6)

        nuevo_estudiante = Estudiante(
            nombre="Alfredito", 
            sexo="M", 
            email='email@bienformado.com', 
            ciudad_nacimiento = self.ciudad,
            fecha_nacimiento = date_in_future,
            grupo = self.grupo)
        try:
            nuevo_estudiante.full_clean()
            self.fail()
        except Exception as e:
            self.assertEqual(e.__str__(), "{'fecha_nacimiento': ['Indique una fecha en el pasado.']}")