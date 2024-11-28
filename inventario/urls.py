from django.urls import path
from . import views

urlpatterns = [
    # Productos
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    
    # Proveedores
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('proveedores/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/editar/<int:pk>/', views.editar_proveedor, name='editar_proveedor'),
    
    # SOAT
    path('productos/mover-vencidos/<int:pk>/', views.mover_a_vencidos, name='mover_a_vencidos'),
    path('productos/mover-dañados/<int:pk>/', views.mover_a_dañados, name='mover_a_dañados'),
]