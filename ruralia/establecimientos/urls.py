from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_campos, name='lista_campos'),
    path('crear/', views.crear_campo, name='crear_campo'),
    path('<int:campo_id>/editar/', views.editar_campo, name='editar_campo'),
    path('<int:campo_id>/eliminar/', views.eliminar_campo, name='eliminar_campo'),
]
