from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),  # Importamos las URLs de la app usuarios
    path('', lambda request: redirect('login')),  # Redirige la página principal al login
]