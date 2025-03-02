from django.contrib import admin
from .models import Asignatura, Grado, Grupo, GrupoAsignatura


admin.site.register(GrupoAsignatura)


@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('id_asignatura', 'nombre')


@admin.register(Grado)
class GradoAdmin(admin.ModelAdmin):
    list_display = ('id_grado', 'nombre')


@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('id_grupo', 'nombre', 'id_grado')
