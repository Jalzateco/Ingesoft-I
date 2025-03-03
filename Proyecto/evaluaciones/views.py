from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Calificacion, Examen, Opcion, Pregunta, Respuesta
from .serializers import CalificacionSerializer, ExamenSerializer, OpcionSerializer, PreguntaSerializer, RespuestaSerializer
from usuarios.permissions import EsDocente, EsEstudiante


class ExamenListView(ListCreateAPIView):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer
    permission_classes = [AllowAny]


class ExamenDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer
    permission_classes = [AllowAny]


class PreguntaListView(ListCreateAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    permission_classes = [AllowAny]

class PreguntaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    permission_classes = [AllowAny]


class OpcionListView(ListCreateAPIView):
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer
    permission_classes = [AllowAny]


class OpcionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer
    permission_classes = [AllowAny]


class RespuestaListView(ListCreateAPIView):
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer
    permission_classes = [AllowAny]


class RespuestaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer
    permission_classes = [AllowAny]


class CalificacionListView(ListCreateAPIView):
    queryset = Calificacion.objects.all()
    serializer_class = OpcionSerializer
    permission_classes = [AllowAny]


class CalificacionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer
    permission_classes = [AllowAny]


class ExamenEstudianteListView(ListAPIView):
    serializer_class = ExamenSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        usuario = self.request.user
        return Examen.objects.filter(grupos=usuario.estudiante.id_grupo)
