from django.contrib import admin
from .models import Docente, Estudiante, Usuario, DocenteAsignatura, DocenteGrupo


admin.register(Docente)
admin.register(Estudiante)
admin.register(Usuario)
admin.register(DocenteAsignatura)
admin.register(DocenteGrupo)