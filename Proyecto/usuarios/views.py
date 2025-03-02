from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Usuario
from .serializers import UsuarioSerializer
from .permissions import EsAdministrador


class UsuarioListView(ListCreateAPIView):
    """
        Solo los administradores pueden listar y crear usuarios.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, EsAdministrador]


class UsuarioDetailView(RetrieveUpdateDestroyAPIView):
    """
        Solo los administradores pueden editar y eliminar usuarios.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, EsAdministrador]