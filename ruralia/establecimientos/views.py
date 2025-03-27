from django.shortcuts import render, redirect, get_object_or_404
from .models import Campo

def lista_campos(request):
    campos = Campo.objects.all()
    return render(request, 'establecimientos/lista_campos.html', {'campos': campos})

def crear_campo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ubicacion = request.POST.get('ubicacion')
        Campo.objects.create(nombre=nombre, ubicacion=ubicacion)
        return redirect('lista_campos')
    return render(request, 'establecimientos/crear_campo.html')

def editar_campo(request, campo_id):
    campo = get_object_or_404(Campo, id=campo_id)
    if request.method == 'POST':
        campo.nombre = request.POST.get('nombre')
        campo.ubicacion = request.POST.get('ubicacion')
        campo.save()
        return redirect('lista_campos')
    return render(request, 'establecimientos/editar_campo.html', {'campo': campo})

def eliminar_campo(request, campo_id):
    campo = get_object_or_404(Campo, id=campo_id)
    if request.method == 'POST':
        campo.delete()
        return redirect('lista_campos')
    return render(request, 'establecimientos/confirmar_eliminar_campo.html', {'campo': campo})
