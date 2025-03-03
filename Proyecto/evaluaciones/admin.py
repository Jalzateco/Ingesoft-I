from django.contrib import admin
from .models import Calificacion, Examen, Opcion, Pregunta, Respuesta, ExamenGrupo, ExamenPregunta


admin.site.register(Calificacion)
admin.site.register(Examen)
admin.site.register(Opcion)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(ExamenGrupo)
admin.site.register(ExamenPregunta)