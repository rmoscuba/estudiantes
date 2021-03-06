from django.db import models

from django.utils import timezone
from datetime import datetime
from dateutil.relativedelta import relativedelta

from django.core.validators import EmailValidator, BaseValidator
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

import studentscrud.utils as utils
from django.conf import settings

@deconstructible
class PastDateValidator():


    def __call__(self, date):
        tz = settings.TIME_ZONE
        now_loc =  utils.to_loc(datetime.now(), tz)
        date_loc = utils.to_loc(date, tz)
        if  now_loc < date_loc:
            raise ValidationError("Indique una fecha en el pasado.")

# Ciudades
class Ciudad(models.Model):

    def __str__(self):
        return self.nombre

    nombre = models.CharField(max_length=200)

# Profesores
class Profesor(models.Model):

    def __str__(self):
        return self.nombre

    nombre = models.CharField(max_length=200)

# Existen grupos que contienen una lista de estudiantes.
# El grupo tiene: nombre, profesor guía.
class Grupo(models.Model):

    def __str__(self):
        return self.nombre

    nombre = models.CharField(max_length=200)
    profesor_guia = models.ForeignKey(Profesor, verbose_name='Profesor guía', on_delete=models.RESTRICT)

# Cada estudiante tiene edad, sexo, nombre, email, 
# fecha de nacimiento , ciudad de nacimiento y grupo.
class Estudiante(models.Model):

    def __str__(self):
        return self.nombre

    def edad(self):
        edad = relativedelta(timezone.now(), self.fecha_nacimiento)
        return edad.years

    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=200, validators=[EmailValidator()])
    ciudad_nacimiento = models.ForeignKey(Ciudad, verbose_name='Ciudad de nacimiento',  on_delete=models.RESTRICT)
    sexo = models.CharField(max_length=50)
    fecha_nacimiento = models.DateTimeField('Fecha de nacimiento', validators=[PastDateValidator()])
    grupo = models.ForeignKey(Grupo, on_delete=models.RESTRICT)