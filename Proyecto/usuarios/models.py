from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UsuarioManager(BaseUserManager):
    def create_user(self, id_usuario, nombres, apellidos, email, clave, rol):
        if not id_usuario:
            raise ValueError("El usuario debe tener un ID único.")
        
        usuario = self.model(id_usuario=id_usuario, nombres=nombres, apellidos=apellidos, email=email, rol=rol)
        usuario.set_password(clave)
        usuario.save(using=self._db)
        return usuario
    
    def create_superuser(self, id_usuario, nombres, apellidos, email, clave):
        usuario = self.create_user(id_usuario, nombres, apellidos, email, clave, rol='Administrador')
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.save(using=self._db)
        return usuario


class Usuario(AbstractBaseUser, PermissionsMixin):
    ROLES = [
        ('Administrador', 'Administrador'),
        ('Docente', 'Docente'),
        ('Estudiante', 'Estudiante')
    ]
    
    id_usuario = models.CharField(max_length=20, primary_key=True) # Cédula o tarjeta de identidad
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=20, choices=ROLES)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_permissions',
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_permissions',
        blank=True
    )
    
    objects = UsuarioManager()
    
    USERNAME_FIELD = 'id_usuario'
    REQUIRED_FIELDS = ['nombres', 'apellidos', 'email']
    
    def __str__(self):
        return f'{self.nombres} {self.apellidos} ({self.rol})'


class Docente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)


class Estudiante(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    promedio_global = models.FloatField(default=0.0)
