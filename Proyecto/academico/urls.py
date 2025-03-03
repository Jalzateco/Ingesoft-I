from django.urls import path
from .views import GradoListView, GradoDetailView, AsignaturaListView, AsignaturaDetailView, GrupoListView, GrupoDetailView


app_name = 'academico'

urlpatterns = [
    path('grados/', GradoListView.as_view(), name='lista-grados'),
    path('grados/<int:pk>/', GradoDetailView.as_view(), name='detalle-grado'),
    path('asignaturas/', AsignaturaListView.as_view(), name='lista-asignaturas'),
    path('asignaturas/<int:pk>/', AsignaturaDetailView.as_view(), name='detalle-asignatura'),
    path('grupos/', GrupoListView.as_view(), name='lista-grupos'),
    path('grupos/<int:pk>/', GrupoDetailView.as_view(), name='detalle-grupo'),
]
