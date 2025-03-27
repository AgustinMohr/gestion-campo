from django.db import models
from django.db import models

class Campo(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
