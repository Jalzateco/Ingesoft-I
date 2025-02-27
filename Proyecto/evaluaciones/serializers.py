from rest_framework import serializers
from .models import Examen, ExamenGrupo, ExamenPregunta, Opcion, Pregunta, Respuesta
from academico.models import Grupo


class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcion
        fields = ('num_opcion', 'texto_opcion')


class PreguntaSerializer(serializers.ModelSerializer):
    opciones = OpcionSerializer(many=True, read_only=True)

    class Meta:
        model = Pregunta
        fields = ('id_pregunta', 'enunciado', 'tipo', 'opciones')


class ExamenPreguntaSerializer(serializers.ModelSerializer):
    id_pregunta = PreguntaSerializer(read_only=True)
    
    class Meta:
        model = ExamenPregunta
        fields = ('id_pregunta',)


class ExamenGrupoSerializer(serializers.ModelSerializer):
    id_grupo = serializers.SlugRelatedField(queryset=Grupo.objects.all(), slug_field='nombre')
    
    class Meta:
        model = ExamenGrupo
        fields = ('id_grupo',)


class ExamenSerializer(serializers.ModelSerializer):
    preguntas = ExamenPreguntaSerializer(many=True, source='examenpregunta_set', read_only=True)
    grupos = ExamenGrupoSerializer(many=True, source='examengrupo_set', read_only=True)
    
    class Meta:
        model = Examen
        fields = ('id_examen', 'titulo', 'descripcion', 'fecha_creacion', 'fecha_aplicacion', 'tiempo_limite', 'aplicada', 'grupos', 'preguntas')


class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = '__all__'
