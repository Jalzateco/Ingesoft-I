from rest_framework import serializers
from .models import Examen, Opcion, Pregunta, Respuesta


class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcion
        fields = ('num_opcion', 'texto_opcion')


class PreguntaSerializer(serializers.ModelSerializer):
    opciones = OpcionSerializer(many=True, read_only=True)

    class Meta:
        model = Pregunta
        fields = ('id_pregunta', 'enunciado','tipo', 'opciones')


class ExamenSerializer(serializers.ModelSerializer):
    preguntas = PreguntaSerializer(many=True, read_only=True) # 
    grupos = serializers.SlugRelatedField(many=True, read_only=True, slug_field='nombre')
    
    class Meta:
        model = Examen
        fields = '__all__'


class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = '__all__'