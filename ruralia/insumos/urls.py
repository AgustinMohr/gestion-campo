from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_remito, name='crear_remito'),
    path('agregar/<int:remito_id>/', views.agregar_insumos, name='agregar_insumos'),
    path('stock/', views.ver_stock, name='ver_stock'),
    path('crear_insumo/', views.crear_insumo, name='crear_insumo'),
    path('ver_insumos/', views.ver_insumos, name='ver_insumos'),
    path('crear_remito/', views.crear_remito, name='crear_remito'),
    path('ver_remito/<int:remito_id>/', views.ver_remito, name='ver_remito'),

]
