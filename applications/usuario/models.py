from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UsuarioManager

# Create your models here.

class Departamento(models.Model):
    nombre = models.CharField('Nombre', max_length=50)

    def __str__(self):
        return str(self.id) + ' ' + self.nombre

class Usuario(AbstractBaseUser, PermissionsMixin):

    NIVEL_CHOICES = (
        ('0', 'Administrador'),
        ('1', 'Coordinador'),
    )

    ESTATUS_CHOICES = (
        ('0', 'Activo'),
        ('1', 'Anulado'),
    )

    username = models.CharField('Nombre de Usuario', max_length=20, unique=True)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)
    nivel = models.CharField(max_length=1, choices=NIVEL_CHOICES, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    estatus = models.CharField('Estatus', max_length=1, choices=ESTATUS_CHOICES)
    foto = models.ImageField(upload_to='medicos',blank=True, null=True)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['nombre','apellido']
    
    objects = UsuarioManager()


    def get_full_name(self):
        return self.nombre + ' ' + self.apellido
    
    def __str__(self):
        return str(self.id) + ' ' + self.username