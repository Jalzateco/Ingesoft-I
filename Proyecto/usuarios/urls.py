from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UsuarioListView, UsuarioDetailView


app_name = 'usuarios'

urlpatterns = [
    path('', UsuarioListView.as_view(), name='lista-usuarios'),
    path('<str:pk>/', UsuarioDetailView.as_view(), name='detalle-usuario'),
    path('login/', TokenObtainPairView.as_view(), name='iniciar-sesion'),
    path('refresh/', TokenRefreshView.as_view(), name='renovar-token'),
]
