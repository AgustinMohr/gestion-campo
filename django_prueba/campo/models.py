
# Create your models here.
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Stock actual
    unidad_medida = models.CharField(max_length=50, choices=[
        ('kg', 'Kilogramos'),
        ('lt', 'Litros'),
        ('un', 'Unidades'),
    ])

    def __str__(self):
        return f"{self.nombre} - {self.cantidad} {self.unidad_medida}"

class MovimientoStock(models.Model):
    TIPO_CHOICES = [
        ('ingreso', 'Ingreso'),
        ('egreso', 'Egreso'),
    ]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="movimientos")
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_movimiento = models.CharField(max_length=10, choices=TIPO_CHOICES)
    fecha = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.tipo_movimiento == 'ingreso':
            self.producto.cantidad += self.cantidad
        elif self.tipo_movimiento == 'egreso':
            if self.producto.cantidad >= self.cantidad:
                self.producto.cantidad -= self.cantidad
            else:
                raise ValueError("No hay suficiente stock para esta operación")

        self.producto.save()  # Guardar el cambio en el stock
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tipo_movimiento} de {self.cantidad} {self.producto.unidad_medida} de {self.producto.nombre}"

class Lote(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    superficie = models.DecimalField(max_digits=10, decimal_places=2, help_text="Superficie en hectáreas")
    
    def __str__(self):
        return f"{self.nombre} ({self.superficie} ha)"


class Aplicacion(models.Model):
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_usada = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Registrar la salida del stock como un "egreso"
        movimiento = MovimientoStock(
            producto=self.producto,
            cantidad=self.cantidad_usada,
            tipo_movimiento='egreso'
        )
        movimiento.save()  # Esto actualizará automáticamente el stock del producto

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Aplicación de {self.cantidad_usada} {self.producto.unidad_medida} de {self.producto.nombre} en {self.lote.nombre} ({self.fecha})"
