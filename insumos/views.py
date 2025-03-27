from django.shortcuts import render, redirect
from .models import Remito, RemitoInsumo, Insumo
from .forms import RemitoForm, RemitoInsumoForm
from .forms import InsumoForm

# Vista para crear un remito
def crear_remito(request):
    if request.method == 'POST':
        remito_form = RemitoForm(request.POST)
        if remito_form.is_valid():
            remito = remito_form.save()  # Guardamos el remito
            # Los insumos ya se asocian automáticamente por el campo 'insumos'
            return redirect('ver_remito', remito_id=remito.id)
    else:
        remito_form = RemitoForm()

    return render(request, 'insumos/crear_remito.html', {'remito_form': remito_form})


# Vista para agregar insumos al remito
def agregar_insumos(request, remito_id):
    remito = Remito.objects.get(id=remito_id)
    if request.method == 'POST':
        form = RemitoInsumoForm(request.POST)
        if form.is_valid():
            remito_insumo = form.save(commit=False)
            remito_insumo.remito = remito
            remito_insumo.save()
            # Actualizar el stock de insumo
            insumo = remito_insumo.insumo
            insumo.cantidad_stock += remito_insumo.cantidad
            insumo.save()
            return redirect('agregar_insumos', remito_id=remito.id)
    else:
        form = RemitoInsumoForm()
    return render(request, 'insumos/agregar_insumos.html', {'form': form, 'remito': remito})

# Vista para mostrar el stock de insumos
def ver_stock(request):
    remitos = Remito.objects.all()  # Obtenemos todos los remitos
    return render(request, 'insumos/ver_stock.html', {'remitos': remitos})

# Vista para crear un insumo

def crear_insumo(request):
    if request.method == 'POST':
        insumo_form = InsumoForm(request.POST)
        if insumo_form.is_valid():
            insumo_form.save()  # Guardamos el insumo en la base de datos
            return redirect('ver_insumos')  # Redirige a la vista que lista los insumos

    else:
        insumo_form = InsumoForm()

    return render(request, 'insumos/crear_insumo.html', {'insumo_form': insumo_form})

# Vista para listar los insumos

def ver_insumos(request):
    insumos = Insumo.objects.all()  # Obtener todos los insumos
    return render(request, 'insumos/ver_insumos.html', {'insumos': insumos})

def ver_remito(request, remito_id):
    remito = Remito.objects.get(id=remito_id)
    return render(request, 'insumos/ver_remito.html', {'remito': remito})