from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from academico.models import Asignatura, Grupo
from .models import Docente, Estudiante, Usuario, DocenteAsignatura, DocenteGrupo


class UsuarioSerializer(serializers.ModelSerializer):
    """
        Serializer para el modelo Usuario, incluyendo manejo de contraseña.
    """
    clave = serializers.CharField(write_only=True)
    
    class Meta:
        model = Usuario
        fields = ('id_usuario', 'nombres', 'apellidos', 'email', 'rol', 'clave')
    
    def create(self, validated_data):
        clave = validated_data.pop('clave')
        usuario = Usuario(**validated_data) # Desempaqueta el diccionario
        usuario.set_password(clave) # Cifra la clave
        usuario.save()
        return usuario
    
    def validate_clave(self, value):
        validate_password(value) # Validación de la seguridad de la clave con Django
        return value


class DocenteAsignaturaSerializer(serializers.ModelSerializer):
    asignatura = serializers.SlugRelatedField(slug_field='nombre', queryset=Asignatura.objects.all())
    
    class Meta:
        model = DocenteAsignatura
        fields = ('asignatura',)


class DocenteGrupoSerializer(serializers.ModelSerializer):
    grupo = serializers.SlugRelatedField(slug_field='nombre', queryset=Grupo.objects.all())
    
    class Meta:
        model = DocenteGrupo
        fields = ('grupo',)


class DocenteSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    asignaturas = DocenteAsignaturaSerializer(many=True, source='docenteasignatura_set', read_only=True)
    grupos = DocenteGrupoSerializer(many=True, source='docentegrupo_set', read_only=True)

    class Meta:
        model = Docente
        fields = ('usuario', 'asignaturas', 'grupos')


class EstudianteSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    id_grupo = serializers.SlugRelatedField(slug_field='nombre', queryset=Grupo.objects.all())

    class Meta:
        model = Estudiante
        fields = ('usuario', 'promedio_global', 'id_grupo')
