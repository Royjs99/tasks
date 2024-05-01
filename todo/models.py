from django.db import models

# Create your models here.


class Task(models.Model):
    tarea = models.CharField(max_length=256)
    priority = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.id}: {self.tarea} the priority is {self.priority}"
    