from desafioadl.models import Tarea, SubTarea
from django.db import connection

def crear_nueva_tarea():
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO desafioadl_tarea(descripcion, eliminada) values(%s, %s)", ['Hacer la tarea 1', 'FALSE'])
    row = cursor.fetchone()
    return row
    #    row = cursor.fetchall()
    #     cursor.execute(sql, (descripcion, eliminada))
    #     id_nueva_tarea = cursor.fetchone()[0]
    # return Tarea(id=id_nueva_tarea, descripcion=descripcion, eliminada=eliminada)


    # p1 = Tarea(descripcion, eliminada)
    # p1.save()
    # p1 = Tarea.objects.create(descripcion='Hacer la tarea 1', eliminada='FALSE')
    # p2 = Tarea.objects.create(descripcion='Hacer la tarea 2', eliminada='FALSE')
    # print(f'Tarea 1: {p1}, Tarea2: {p2}')

def crear_sub_tarea(descripcion, eliminada, tarea_id):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO desafioadl_subtarea(descripcion, eliminada, tarea_id) values(%s, %s, %s)", ['Hacer la subtarea 1', 'FALSE', '1'])
        row = cursor.fetchone()
    return row
    # p1 = SubTarea(descripcion, eliminada, tarea_id)
    # p1.save()
    # p1 = SubTarea.objects.create(descripcion='Hacer la tarea 1', eliminada='FALSE',tarea_id='1')
    # p2 = SubTarea.objects.create(descripcion='Hacer la tarea 2', eliminada='FALSE', tarea_id='2')
    # print(f'SuTarea 1: {p1}, SuTarea2: {p2}')

def recupera_tareas_y_sub_tareas(id=None):
    lista_de_tareas = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM desafioadl_tareas")
        row = cursor.fetchall()
        for p in row:
            lista_de_tareas.append(Tarea(*p))
    return lista_de_tareas
    
    # if id is None:
    #     print(f'Tareas: {Tarea.objects.all()}, SuTareas: {SubTarea.objects.all()}')
    # else:
    #     try:
    #         print(f'Tareas: {Tarea.objects.all(pk=id)}, SuTareas: {SubTarea.objects.all(pk=id)}')
    #     except Tarea.DoesNotExist:
    #        print("La tarea con el ID dado no existe.")

def elimina_tarea(id=None):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM desafioadl_tareas WHERE id= %s", [str(id)])
        row = cursor.fetchone()
    return row
    # if id is None:
    #     print("Debe indicar ID de la Tarea.")
    # else:
    #     p1 = Tarea.objects.delete(pk=id)

def elimina_sub_tarea():
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM desafioadl_subtareas WHERE id= %s", [str(id)])
        row = cursor.fetchone()
    return row
    # if id is None:
    #     print("Debe indicar ID de la SubTarea.")
    # else:
    #     p1 = SubTarea.objects.delete(pk=id)
    
def imprimir_en_pantalla():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM desafioadl_tarea")
        row = cursor.fetchall()
        for p in row:
            print(str(p[0]) + ' - ' + p[1] + ' ' + p[2])
#    print(f'Tareas: {Tarea.objects.all()}, SuTareas: {SubTarea.objects.all()}')
    
    