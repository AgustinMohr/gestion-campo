from django.db import models

# Modelo para el insumo
from django.db import models

class Insumo(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Agregar precio
    unidad = models.CharField(max_length=50)  # Agregar unidad

    def __str__(self):
        return self.nombre

# Modelo para el remito
class Remito(models.Model):
    numero_remito = models.CharField(max_length=100)
    proveedor = models.CharField(max_length=100)
    fecha = models.DateField(auto_now=False, auto_now_add=False, blank=False, null=False)  # editable
    # otros campos"

# Relación entre Remito y los insumos entregados
class RemitoInsumo(models.Model):
    remito = models.ForeignKey(Remito, on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} {self.insumo.nombre} en Remito {self.remito.numero_remito}"

