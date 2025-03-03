from django.db import models


class Asignatura(models.Model):
    
    class Meta:
        verbose_name_plural = "Asignaturas"
        verbose_name = "Asignatura"
        ordering = ["nombre"]
    
    id_asignatura = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre


class Grado(models.Model):
    
    class Meta:
        verbose_name_plural = "Grados"
        verbose_name = "Grado"
        ordering = ["nombre"]
    
    id_grado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre


class Grupo(models.Model):
    
    class Meta:
        verbose_name_plural = "Grupos"
        verbose_name = "Grupo"
        ordering = ["nombre"]
    
    id_grupo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    
    id_grado = models.ForeignKey(Grado, on_delete=models.CASCADE, related_name='grado')
    asignaturas_asignadas = models.ManyToManyField('Asignatura', through='GrupoAsignatura')
    
    def __str__(self):
        return f"{self.nombre} - {self.id_grado}"


class GrupoAsignatura(models.Model):
    id_grupo = models.ForeignKey('Grupo', on_delete=models.CASCADE)
    id_asignatura = models.ForeignKey('Asignatura', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('id_grupo', 'id_asignatura')
