from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
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


