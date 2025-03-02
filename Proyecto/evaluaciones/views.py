from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Calificacion, Examen, Opcion, Pregunta, Respuesta
from .serializers import CalificacionSerializer, ExamenSerializer, OpcionSerializer, PreguntaSerializer, RespuestaSerializer
from usuarios.permissions import EsDocente, EsEstudiante


# CRUD para exámenes (Solo docentes)
class ExamenListView(ListCreateAPIView):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer
    permission_classes = [IsAuthenticated, EsDocente]


class ExamenDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer
    permission_classes = [IsAuthenticated, EsDocente]


# CRUD Pregunta por Examen (Solo docentes)
class PreguntaListView(ListCreateAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    permission_classes = [IsAuthenticated, EsDocente]


class PreguntaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    permission_classes = [IsAuthenticated, EsDocente]


# CRUD para Opciones (Solo docentes)
class OpcionListView(ListCreateAPIView):
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer
    permission_classes = [IsAuthenticated, EsDocente]


class OpcionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer
    permission_classes = [IsAuthenticated, EsDocente]


class RespuestaListView(ListCreateAPIView):
    """
        Los estudiantes envían respuestas. Si todas son de opción múltiple,
        se calcula la calificación automáticamente.
    """
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer
    permission_classes = [IsAuthenticated, EsEstudiante]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        usuario = request.user
        examen_id = request.data.get('id_examen')

        if not examen_id:
            return response  # No se puede procesar sin un examen

        # Verificar si el estudiante respondió todas las preguntas
        examen = Examen.objects.get(id_examen=examen_id)
        preguntas_del_examen = examen.preguntas.all()
        respuestas_del_estudiante = Respuesta.objects.filter(id_examen=examen, id_usuario=usuario)

        # **Actualizar calificación parcial basada en las opciones correctas**
        for respuesta in respuestas_del_estudiante:
            pregunta = respuesta.id_pregunta

            if pregunta.tipo == 'opcion-multiple' and respuesta.num_opcion is not None:
                # Obtener la opción seleccionada
                opcion_seleccionada = Opcion.objects.filter(id_pregunta=pregunta, num_opcion=respuesta.num_opcion).first()
                if opcion_seleccionada and opcion_seleccionada.es_correcta:
                    respuesta.calificacion_parcial = opcion_seleccionada.peso_calificacion
                else:
                    respuesta.calificacion_parcial = 0.0  # No obtiene puntos si la opción es incorrecta

                respuesta.save()

        # **Si todas las respuestas fueron enviadas, verificar si hay preguntas abiertas**
        if respuestas_del_estudiante.count() == preguntas_del_examen.count():
            preguntas_abiertas = preguntas_del_examen.filter(tipo='abierta')

            if not preguntas_abiertas.exists():
                # Calificación automática si todas las preguntas son de opción múltiple
                nota_final = sum(r.calificacion_parcial for r in respuestas_del_estudiante)
                Calificacion.objects.create(id_examen=examen, id_usuario=usuario, nota=nota_final)
            else:
                # Se espera revisión del docente
                Calificacion.objects.create(id_examen=examen, id_usuario=usuario, nota=0.0)  # Temporalmente en 0

        return response


class RespuestaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer
    permission_classes = [IsAuthenticated, EsDocente]  # Solo docentes pueden modificar respuestas


# CRUD para Calificaciones (Solo docentes pueden asignar/modificar)
class CalificacionListView(ListCreateAPIView):
    """
        Docentes pueden ver todas las calificaciones, estudiantes solo las suyas.
    """
    serializer_class = CalificacionSerializer

    def get_queryset(self):
        usuario = self.request.user
        if usuario.rol == 'Estudiante':
            return Calificacion.objects.filter(id_usuario=usuario)
        return Calificacion.objects.all()  # Docentes ven todas las calificaciones

    def get_permissions(self):
        if self.request.method == 'POST':  # Solo docentes pueden asignar calificaciones
            return [IsAuthenticated(), EsDocente()]
        return [IsAuthenticated()]  # Estudiantes pueden ver sus calificaciones


class CalificacionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer
    permission_classes = [IsAuthenticated, EsDocente]


class CalificacionUpdateView(RetrieveUpdateAPIView):
    """
        Los docentes solo pueden calificar preguntas abiertas y recalcular la calificación final.
    """
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer
    permission_classes = [IsAuthenticated, EsDocente]

    def update(self, request, *args, **kwargs):
        calificacion = self.get_object()
        usuario = request.user

        # Verificar que el usuario sea docente
        if usuario.rol != 'Docente':
            return Response({'error': 'No tienes permisos para modificar esta calificación'}, status=403)

        # Obtener las respuestas abiertas del examen de este estudiante
        respuestas_abiertas = Respuesta.objects.filter(
            id_examen=calificacion.id_examen,
            id_usuario=calificacion.id_usuario,
            id_pregunta__tipo='abierta'
        )

        # Verificar que el docente solo está modificando preguntas abiertas
        for respuesta in respuestas_abiertas:
            nueva_calificacion = request.data.get(f'calificacion_{respuesta.id_respuesta}')
            if nueva_calificacion is not None:
                respuesta.calificacion_parcial = nueva_calificacion
                respuesta.save()

        # **Recalcular la calificación total**
        respuestas_del_estudiante = Respuesta.objects.filter(
            id_examen=calificacion.id_examen, id_usuario=calificacion.id_usuario
        )
        calificacion.nota = sum(r.calificacion_parcial for r in respuestas_del_estudiante)
        calificacion.save()

        return Response({
            'mensaje': 'Calificación actualizada correctamente',
            'nota_final': calificacion.nota
        })


class ExamenEstudianteListView(ListAPIView):
    """
        Solo los estudiantes pueden ver exámenes asignados a su grupo.
    """
    serializer_class = ExamenSerializer
    permission_classes = [IsAuthenticated, EsEstudiante]

    def get_queryset(self):
        usuario = self.request.user
        return Examen.objects.filter(grupos=usuario.estudiante.id_grupo)
