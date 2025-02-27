from django.db import models


class Examen(models.Model):
    id_examen = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_aplicacion = models.DateTimeField(blank=True, null=True)
    tiempo_limite = models.IntegerField(blank=True, null=True)
    aplicada = models.BooleanField(default=False)
    
    preguntas = models.ManyToManyField('Pregunta', through='ExamenPregunta')
    grupos = models.ManyToManyField('academico.Grupo', through='ExamenGrupo')
    
    def __str__(self):
        return self.titulo


class Pregunta(models.Model):
    TIPOS_PREGUNTA = [
        ('opcion-multiple', 'Opción múltiple'),
        ('abierta', 'Abierta'),
    ]
    
    id_pregunta = models.AutoField(primary_key=True)
    enunciado = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPOS_PREGUNTA)
    
    def __str__(self):
        return f'{self.id_pregunta} - {self.enunciado}'


class Opcion(models.Model):
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='opciones')
    num_opcion = models.PositiveIntegerField()
    texto_opcion = models.TextField()
    es_correcta = models.BooleanField(default=False)
    peso_calificacion = models.FloatField(default=0.0)
    
    class Meta:
        unique_together = ('id_pregunta', 'num_opcion')
    
    def __str__(self):
        return f'{self.id_pregunta.id_pregunta}.{self.num_opcion} - {self.texto_opcion}'


class Respuesta(models.Model):
    id_respuesta = models.AutoField(primary_key=True)
    id_examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    id_usuario = models.IntegerField() # Relacionar luego con el modelo de usuario
    num_opcion = models.IntegerField(blank=True, null=True)
    respuesta_abierta = models.TextField(blank=True, null=True)
    calificacion_parcial = models.FloatField(default=0.0)
    
    def __str__(self):
        return f'Usuario: {self.id_usuario} - Examen, Pregunta: {self.id_examen.id_examen}, {self.id_pregunta.id_pregunta}'


# IMPLEMENTAR AQUÍ MODELO DE CALIFICACIONES


class ExamenPregunta(models.Model):
    id_examen = models.ForeignKey('Examen', on_delete=models.CASCADE)
    id_pregunta = models.ForeignKey('Pregunta', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('id_examen', 'id_pregunta')
    
    def __str__(self):
        return f"Pregunta {self.id_pregunta.id_pregunta} en {self.id_examen.titulo}"


class ExamenGrupo(models.Model):
    id_examen = models.ForeignKey('Examen', on_delete=models.CASCADE)
    id_grupo = models.ForeignKey('academico.Grupo', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('id_examen', 'id_grupo')
    
    def __str__(self):
        return f"{self.id_examen.titulo} - {self.id_grupo.nombre}"