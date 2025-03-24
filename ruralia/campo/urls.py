from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, MovimientoStockViewSet, LoteViewSet, AplicacionViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'movimientos', MovimientoStockViewSet)
router.register(r'lotes', LoteViewSet)
router.register(r'aplicaciones', AplicacionViewSet)

urlpatterns = [
    path('home/', views.index, name='index'),  # Aquí defines la URL asociada con 'index'
    path('api/',include(router.urls)),
    path('app/',views.app, name='app'),

    path('productos/lista', views.lista_productos, name='lista_productos'),
    path('productos/alta/', views.alta_producto, name='alta_producto'), 

    path('productos/', views.lista_productos2, name='lista_productos2'),
    path('productos/create/', views.crear_producto, name='crear_producto'),  # Crear producto
    path('productos/<int:pk>/update/', views.actualizar_producto, name='actualizar_producto'),  # Actualizar producto
    path('productos/<int:pk>/delete/', views.eliminar_producto, name='eliminar_producto'),  # Eliminar producto

]