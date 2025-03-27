from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_lotes, name='lista_lotes'),
    path('crear/', views.crear_lote, name='crear_lote'),
    path('campo/<int:campo_id>/', views.lotes_por_campo, name='lotes_por_campo'),
    path('<int:lote_id>/editar/', views.editar_lote, name='editar_lote'),
    path('<int:lote_id>/eliminar/', views.eliminar_lote, name='eliminar_lote'),
    path('<int:lote_id>/', views.detalle_lote, name='detalle_lote'),
]
