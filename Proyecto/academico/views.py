from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Asignatura, Grado, Grupo
from .serializers import AsignaturaSerializer, GradoSerializer, GrupoSerializer
from usuarios.permissions import EsAdministrador


# CRUD para Grados (Solo administradores pueden gestionar)
class GradoListView(ListCreateAPIView):
    queryset = Grado.objects.all()
    serializer_class = GradoSerializer
    permission_classes = [IsAuthenticated, EsAdministrador]


class GradoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Grado.objects.all()
    serializer_class = GradoSerializer
    permission_classes = [IsAuthenticated, EsAdministrador]


# CRUD para Asignaturas (Solo administradores pueden gestionar)
class AsignaturaListView(ListCreateAPIView):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer
    permission_classes = [IsAuthenticated, EsAdministrador]


class AsignaturaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer
    permission_classes = [IsAuthenticated, EsAdministrador]


# CRUD para Grupos (Solo administradores pueden gestionar)
class GrupoListView(ListCreateAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    permission_classes = [IsAuthenticated, EsAdministrador]

class GrupoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    permission_classes = [IsAuthenticated, EsAdministrador]
