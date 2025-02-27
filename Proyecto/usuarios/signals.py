from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Docente, Estudiante, Usuario


@receiver(post_save, sender=Usuario)
def crear_especializacion_usuario(sender, instance, created, **kwargs):
    if created:
        if instance.rol == "Estudiante":
            Estudiante.objects.create(usuario=instance)
        elif instance.rol == "Docente":
            Docente.objects.create(usuario=instance)
