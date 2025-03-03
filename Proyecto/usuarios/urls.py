from django.urls import path
from .views import UsuarioListView, UsuarioDetailView


app_name = 'usuarios'

urlpatterns = [
    path('', UsuarioListView.as_view(), name='lista-usuarios'),
    path('<str:pk>/', UsuarioDetailView.as_view(), name='detalle-usuario'),
]
