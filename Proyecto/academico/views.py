from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Asignatura, Grado, Grupo
from .serializers import AsignaturaSerializer, GradoSerializer, GrupoSerializer
from usuarios.permissions import EsAdministrador


class GradoListView(ListCreateAPIView):
    queryset = Grado.objects.all()
    serializer_class = GradoSerializer
    permission_classes = [AllowAny]


class GradoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Grado.objects.all()
    serializer_class = GradoSerializer
    permission_classes = [AllowAny]


class AsignaturaListView(ListCreateAPIView):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer
    permission_classes = [AllowAny]


class AsignaturaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer
    permission_classes = [AllowAny]


class GrupoListView(ListCreateAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    permission_classes = [AllowAny]


class GrupoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    permission_classes = [AllowAny]