from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class HistorialSMS(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    destinatario = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=260)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' > ' + self.destinatario

    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'


class CuentaTwilio(models.Model):
    nombre = models.CharField(max_length=100)
    account = models.CharField(max_length=100)
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Telefono(models.Model):
    telefono = models.CharField(max_length=20)
    cuenta = models.ForeignKey(CuentaTwilio, on_delete=models.CASCADE)

    def __str__(self):
        return '[' + self.cuenta.nombre + ']' + self.telefono

