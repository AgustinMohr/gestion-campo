from django.db import models
from establecimientos.models import Campo  # Importamos el modelo Campo

class Lote(models.Model):
    campo = models.ForeignKey(Campo, on_delete=models.CASCADE, related_name="lotes")
    nombre = models.CharField(max_length=100)
    superficie = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} ({self.campo.nombre})"