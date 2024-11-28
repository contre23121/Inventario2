from django import forms
from .models import Producto, Categoria, Proveedor, ProductosVencidos, ProductosDañados

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad_por_caja', 
                 'cantidad_por_unidad', 'categoriaid', 'proveedorid']
        labels = {
            'nombre': 'Nombre del Producto',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'cantidad_por_caja': 'Cantidad por Caja',
            'cantidad_por_unidad': 'Cantidad por Unidad',
            'categoriaid': 'Categoría',
            'proveedorid': 'Proveedor'
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'direccion', 'telefono', 'email']

class ProductoVencidoForm(forms.ModelForm):
    class Meta:
        model = ProductosVencidos
        fields = ['cantidad', 'fecha_vencimiento']

class ProductoDañadoForm(forms.ModelForm):
    class Meta:
        model = ProductosDañados
        fields = ['cantidad', 'descripcion']