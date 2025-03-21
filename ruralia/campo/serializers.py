from rest_framework import serializers
from rest_framework.fields import CharField, EmailField, DecimalField
from .models import Producto, MovimientoStock, Lote, Aplicacion


class ProductoSerializer(serializers.ModelSerializer):
    nombre = CharField(source="nombre", required=True)
    descripcion = CharField(source="descripcion", required=True)
    cantidad = DecimalField(source="cantidad", required=True, max_digits=10, decimal_places=2)
    
    class Meta:
        model = Producto
        fields = (
			'nombre',
			'descripcion',
			'cantidad'
		)

class MovimientoStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoStock
        fields = '__all__'

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'

class AplicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aplicacion
        fields = '__all__'
