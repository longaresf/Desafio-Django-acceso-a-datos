from desafioadl.models import Tarea, SubTarea
from django.db import models

def crear_nueva_tarea(descripcion_tarea, eliminada_tarea):
    nueva_tarea = Tarea.objects.create(descripcion=descripcion_tarea, eliminada=eliminada_tarea)
    return nueva_tarea

def crear_sub_tarea(descripcion_subtarea, eliminada_subtarea, tarea_id):
    nueva_tarea_id = Tarea.objects.get(pk=tarea_id)
    nueva_subtarea = SubTarea.objects.create(descripcion=descripcion_subtarea, eliminada=eliminada_subtarea, **{'tarea_id': nueva_tarea_id})
    return nueva_subtarea

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.all()
    subtareas = SubTarea.objects.all()
    return tareas, subtareas

def elimina_tarea(tarea_id):
    tarea_id_eliminar = Tarea.objects.get(pk=tarea_id)
    tarea_id_eliminar.delete()
    return tarea_id_eliminar

def elimina_sub_tarea(subtarea_id):
    subtarea_id_eliminar = SubTarea.objects.get(pk=subtarea_id)
    subtarea_id_eliminar.delete()
    return subtarea_id_eliminar

def imprimir_en_pantalla(tareas, subtareas):
    subtareas = SubTarea.objects.all()
    for t in subtareas:
        print(f"Descripción de la tarea : {t.tarea_id.descripcion}, Eliminada: {t.tarea_id.eliminada}, Subtarea Descripción : {t.descripcion}")
