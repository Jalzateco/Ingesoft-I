from rest_framework import serializers
from .models import Asignatura, Grado, Grupo, GrupoAsignatura


class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'


class GradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grado
        fields = '__all__'


class GrupoSerializer(serializers.ModelSerializer):
    id_grado = serializers.SlugRelatedField(queryset=Grado.objects.all(), slug_field='nombre')
    asignaturas_asignadas = AsignaturaSerializer(many=True, read_only=True, source='asignaturas_asignadas.all')
    
    class Meta:
        model = Grupo
        fields = '__all__'


class GrupoAsignaturaSerializer(serializers.ModelSerializer):
    id_grupo = serializers.SlugRelatedField(queryset=Grupo.objects.all(), slug_field='nombre')
    id_asignatura = serializers.SlugRelatedField(queryset=Asignatura.objects.all(), slug_field='nombre')
    
    class Meta:
        model = GrupoAsignatura
        fields = '__all__'
