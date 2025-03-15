from django.urls import path
from . import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, MovimientoStockViewSet, LoteViewSet, AplicacionViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'movimientos', MovimientoStockViewSet)
router.register(r'lotes', LoteViewSet)
router.register(r'aplicaciones', AplicacionViewSet)

urlpatterns = [
    path('',views.indice, name='indice'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/alta/', views.alta_producto, name='alta_producto'), 
]