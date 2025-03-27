from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Lote
from establecimientos.models import Campo

def lotes_por_campo(request, campo_id):
    campo = get_object_or_404(Campo, id=campo_id)
    lotes = Lote.objects.filter(campo=campo)
    return render(request, 'lotes/lotes_por_campo.html', {'campo': campo, 'lotes': lotes})

from django.contrib import messages
from establecimientos.models import Campo
from .models import Lote

def crear_lote(request):
    campos = Campo.objects.all()
    campo_id_preseleccionado = request.GET.get('campo_id', '')

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        superficie = request.POST.get('superficie')
        campo_id = request.POST.get('campo')

        try:
            campo = Campo.objects.get(id=int(campo_id))
        except (Campo.DoesNotExist, ValueError):
            messages.error(request, "⚠️ El campo seleccionado no existe o es inválido.")
            return render(request, 'lotes/crear_lote.html', {
                'campos': campos,
                'campo_id_preseleccionado': campo_id
            })

        Lote.objects.create(nombre=nombre, superficie=superficie, campo=campo)
        messages.success(request, f"✅ Lote '{nombre}' creado correctamente.")
        return redirect('lotes_por_campo', campo_id=campo.id)

    return render(request, 'lotes/crear_lote.html', {
        'campos': campos,
        'campo_id_preseleccionado': campo_id_preseleccionado
    })

def editar_lote(request, lote_id):
    lote = get_object_or_404(Lote, id=lote_id)
    campos = Campo.objects.all()
    if request.method == 'POST':
        lote.nombre = request.POST.get('nombre')
        lote.superficie = request.POST.get('superficie')
        campo_id = request.POST.get('campo')
        lote.campo = get_object_or_404(Campo, id=campo_id)
        lote.save()
        return redirect('lotes_por_campo', campo_id=lote.campo.id)
    return render(request, 'lotes/editar_lote.html', {'lote': lote, 'campos': campos})

def eliminar_lote(request, lote_id):
    lote = get_object_or_404(Lote, id=lote_id)
    campo_id = lote.campo.id
    lote.delete()
    return redirect('lotes_por_campo', campo_id=campo_id)

def lista_lotes(request):
    lotes = Lote.objects.select_related('campo').all()
    return render(request, 'lotes/lista_lotes.html', {'lotes': lotes})

def detalle_lote(request, lote_id):
    lote = get_object_or_404(Lote, id=lote_id)
    return render(request, 'lotes/detalle_lote.html', {'lote': lote})
