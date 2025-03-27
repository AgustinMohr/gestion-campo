from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('', lambda request: redirect('login')),
    path('establecimientos/', include('establecimientos.urls')),
    path('lotes/', include('lotes.urls')),
    path('insumos/', include('insumos.urls')),
]
