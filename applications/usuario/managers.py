from rest_framework.authtoken.models import Token
from django.db import models

from django.contrib.auth.models import BaseUserManager
from django.db.models import Q


class UsuarioManager(BaseUserManager, models.Manager):

    def _create_user(self, username, nombre, apellido, departamento, nivel, password, estatus, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            nombre = nombre,
            apellido = apellido,
            departamento = departamento,
            nivel = nivel,
            password = password,
            estatus = estatus,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        token = Token.objects.create(user=user)
        return token.key

    def create_user(self, username, nombre, apellido, departamento, nivel, estatus=0, password=None, **extra_fields):
        return self._create_user(username, nombre, apellido, departamento, nivel, estatus, password, False, False, **extra_fields)

    def create_superuser(self, username, nombre, apellido, departamento=None, nivel=None, estatus=0, password=None,**extra_fields):
        return self._create_user(username, nombre, apellido, departamento, nivel, password, estatus, True, True, **extra_fields)

    def buscar_usuario(self, kword):
        consulta = self.filter(
            Q(nombre__icontains=kword) | Q(apellido__icontains=kword)
        )
        return consulta