from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Producto, MovimientoStock, Lote, Aplicacion
from .serializers import ProductoSerializer, MovimientoStockSerializer, LoteSerializer, AplicacionSerializer
from .forms import ProductoForm

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class MovimientoStockViewSet(viewsets.ModelViewSet):
    queryset = MovimientoStock.objects.all()
    serializer_class = MovimientoStockSerializer

class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer

class AplicacionViewSet(viewsets.ModelViewSet):
    queryset = Aplicacion.objects.all()
    serializer_class = AplicacionSerializer

def indice(request):
    return render(request, 'base.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})

def alta_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo producto
            return redirect('lista_productos')  # Redirige a la lista de productos
    else:
        form = ProductoForm()

    return render(request, 'productos/alta_producto.html', {'form': form})

from .serializers import ProductoSerializer

@api_view(['GET'])
def lista_productos2(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)  # Devuelve JSON


@api_view(['POST'])
def crear_producto(request):
    if request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)  # Creamos el serializador con los datos enviados
        if serializer.is_valid():  # Validamos los datos
            serializer.save()  # Guardamos el nuevo producto
            return Response(serializer.data, status=201)  # Devolvemos el producto creado con un código 201
        return Response(serializer.errors, status=400)  # Si los datos no son válidos, devolvemos errores con un código 400

@api_view(['PUT'])
def actualizar_producto(request, pk):
    try:
        producto = Producto.objects.get(pk=pk)  # Buscamos el producto por su ID
    except Producto.DoesNotExist:
        return Response({'error': 'Producto no encontrado'}, status=404)

    if request.method == 'PUT':
        serializer = ProductoSerializer(producto, data=request.data)  # Creamos el serializador con los datos nuevos
        if serializer.is_valid():  # Validamos los datos
            serializer.save()  # Guardamos el producto actualizado
            return Response(serializer.data)  # Devolvemos el producto actualizado
        return Response(serializer.errors, status=400)  # Si los datos no son válidos, devolvemos los errores


@api_view(['DELETE'])
def eliminar_producto(request, pk):
    try:
        producto = Producto.objects.get(pk=pk)  # Buscamos el producto por su ID
    except Producto.DoesNotExist:
        return Response({'error': 'Producto no encontrado'}, status=404)

    producto.delete()  # Eliminamos el producto
    return Response({'mensaje': 'Producto eliminado'}, status=204)  # Devolvemos un mensaje de éxito con código 204

