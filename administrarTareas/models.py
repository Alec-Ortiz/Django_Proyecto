from django.db import models

# Create your models here.

class Tareas(models.Model):
    
    nombreTarea = models.CharField(max_length=100)
    descripcionTarea = models.TextField(blank=False)
    
    def __str__(self):
        return self.nombreTarea
    