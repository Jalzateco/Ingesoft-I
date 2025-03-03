from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UsuarioManager(BaseUserManager):
    """
        Manager personalizado para manejar la creación de usuarios y superusuarios.
    """
    
    def create_user(self, id_usuario, nombres, apellidos, email, clave, rol):
        if not id_usuario:
            raise ValueError("El usuario debe tener un ID único.")
        
        usuario = self.model(id_usuario=id_usuario, nombres=nombres, apellidos=apellidos, email=email, rol=rol)
        usuario.set_password(clave)
        usuario.save(using=self._db)
        return usuario
    
    def create_superuser(self, id_usuario, nombres, apellidos, email, password):
        usuario = self.create_user(id_usuario, nombres, apellidos, email, clave=password, rol='Administrador')
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.save(using=self._db)
        return usuario


class Usuario(AbstractBaseUser, PermissionsMixin):
    """
        Modelo de usuario para el sistema SISEXAM.
        Usa la cédula o tarjeta de identidad como identificador único y permite manejar autenticación y permisos.
    """
    objects = UsuarioManager()

    USERNAME_FIELD = 'id_usuario'
    REQUIRED_FIELDS = ['nombres', 'apellidos', 'email']

    def __str__(self):
        return f'{self.nombres} {self.apellidos} ({self.rol})'

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
    """
        Modelo que representa a un docente en el sistema.
    """
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    asignaturas = models.ManyToManyField('academico.Asignatura', through='DocenteAsignatura')
    grupos = models.ManyToManyField('academico.Grupo', through='DocenteGrupo')
    
    def __str__(self):
        return f"Docente: {self.usuario.nombres} {self.usuario.apellidos}"


class DocenteAsignatura(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    asignatura = models.ForeignKey('academico.Asignatura', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('docente', 'asignatura')
    
    def __str__(self):
        return f"Profesor {self.docente.usuario.nombres} {self.docente.usuario.apellidos} - {self.asignatura.nombre}"


class DocenteGrupo(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    grupo = models.ForeignKey('academico.Grupo', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('docente', 'grupo')
    
    def __str__(self):
        return f"{self.docente.usuario.nombres} {self.docente.usuario.nombres} - {self.grupo.nombre}"


class Estudiante(models.Model):
    """
        Modelo que representa a un estudiante en el sistema.
    """
    promedio_global = models.FloatField(default=0.0)
    
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    id_grupo = models.ForeignKey('academico.Grupo', on_delete=models.PROTECT, default=None, null=True, blank=True)
    
    def __str__(self):
        return f"Estudiante: {self.usuario.nombres} {self.usuario.apellidos} - Grupo: {self.id_grupo.nombre}"
