from django.contrib import admin
from django.urls import path, include  # <--- IMPORTAR `include` AQUÍ

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion_usuarios/', include('gestion_usuarios.urls')),  # Tu línea de include
    path('inventario/', include('inventario.urls')),
]
