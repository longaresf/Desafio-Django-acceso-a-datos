from django.db import models

# Create your models here.

class Tarea(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    descripcion = models.CharField(max_length=200, default="")
    eliminada = models.BooleanField(default=False)

class SubTarea(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    descripcion = models.CharField(max_length=200, default="")
    eliminada = models.BooleanField(default=False)
    tarea_id = models.ForeignKey('Tarea', on_delete=models.CASCADE)