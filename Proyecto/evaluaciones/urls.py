from django.urls import path
from .views import (
    ExamenListView, ExamenDetailView, PreguntaListView, PreguntaDetailView,
    OpcionListView, OpcionDetailView, RespuestaListView, RespuestaDetailView,
    CalificacionListView, CalificacionDetailView, ExamenEstudianteListView
)


app_name = 'evaluaciones'

urlpatterns = [
    path('examenes/', ExamenListView.as_view(), name='lista-examenes'),  
    path('examenes/<int:pk>/', ExamenDetailView.as_view(), name='detalle-examen'),
    path('mis-examenes/', ExamenEstudianteListView.as_view(), name='mis-examenes'),
    path('preguntas/', PreguntaListView.as_view(), name='lista-preguntas'),  
    path('preguntas/<int:pk>/', PreguntaDetailView.as_view(), name='detalle-pregunta'),
    path('opciones/', OpcionListView.as_view(), name='lista-opciones'),  
    path('opciones/<int:pk>/', OpcionDetailView.as_view(), name='detalle-opcion'),
    path('respuestas/', RespuestaListView.as_view(), name='lista-respuestas'),  
    path('respuestas/<int:pk>/', RespuestaDetailView.as_view(), name='detalle-respuesta'),
    path('calificaciones/', CalificacionListView.as_view(), name='lista-calificaciones'),  
    path('calificaciones/<int:pk>/', CalificacionDetailView.as_view(), name='detalle-calificacion'),
]
