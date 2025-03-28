from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),  # Importamos las URLs de la app usuarios
    path('', lambda request: redirect('login')),  # Redirige la página principal al login
    path('', include('app_principal.urls')),  # Dashboard y funcionalidades
    path('establecimientos/', include('establecimientos.urls')),
    path('lotes/', include('lotes.urls')),
    path('insumos/', include('insumos.urls')),
]
