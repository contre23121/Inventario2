from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import *
from .forms import *

# Vistas para Productos
@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/productos/lista.html', {'productos': productos})

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            # Registrar en historial
            HistorialInventario.objects.create(
                productoid=producto,
                cantidad=producto.cantidad_por_unidad,
                fecha=timezone.now(),
                tipo_movimiento='Ingreso',
                usuarioid=request.user
            )
            messages.success(request, 'Producto agregado exitosamente')
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'inventario/productos/form.html', {'form': form, 'accion': 'Agregar'})

@login_required
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save()
            # Registrar en historial
            HistorialInventario.objects.create(
                productoid=producto,
                cantidad=producto.cantidad_por_unidad,
                fecha=timezone.now(),
                tipo_movimiento='Modificación',
                usuarioid=request.user
            )
            messages.success(request, 'Producto actualizado exitosamente')
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'inventario/productos/form.html', {'form': form, 'accion': 'Editar'})

@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        # Registrar en historial antes de eliminar
        HistorialInventario.objects.create(
            productoid=producto,
            cantidad=producto.cantidad_por_unidad,
            fecha=timezone.now(),
            tipo_movimiento='Eliminación',
            usuarioid=request.user
        )
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente')
        return redirect('lista_productos')
    return render(request, 'inventario/productos/eliminar.html', {'producto': producto})

# Vistas para Proveedores
@login_required
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'inventario/proveedores/lista.html', {'proveedores': proveedores})

@login_required
def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor agregado exitosamente')
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'inventario/proveedores/form.html', {'form': form, 'accion': 'Agregar'})

@login_required
def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor actualizado exitosamente')
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'inventario/proveedores/form.html', {'form': form, 'accion': 'Editar'})

# Vistas para SOAT (Productos Vencidos y Dañados)
@login_required
def mover_a_vencidos(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoVencidoForm(request.POST)
        if form.is_valid():
            producto_vencido = form.save(commit=False)
            producto_vencido.productoid = producto
            producto_vencido.save()
            
            # Registrar en historial de transferencias
            HistorialTransferenciasDROPS.objects.create(
                productoid=producto,
                cantidad=producto_vencido.cantidad,
                fecha_transferencia=timezone.now(),
                tipo_transferencia='Vencido',
                usuarioid=request.user
            )
            
            messages.success(request, 'Producto movido a vencidos exitosamente')
            return redirect('lista_productos')
    else:
        form = ProductoVencidoForm()
    return render(request, 'inventario/productos/mover_vencidos.html', {'form': form, 'producto': producto})

@login_required
def mover_a_dañados(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoDañadoForm(request.POST)
        if form.is_valid():
            producto_dañado = form.save(commit=False)
            producto_dañado.productoid = producto
            producto_dañado.fecha_reporte = timezone.now()
            producto_dañado.save()
            
            # Registrar en historial de transferencias
            HistorialTransferenciasDROPS.objects.create(
                productoid=producto,
                cantidad=producto_dañado.cantidad,
                fecha_transferencia=timezone.now(),
                tipo_transferencia='Dañado',
                usuarioid=request.user
            )
            
            messages.success(request, 'Producto movido a dañados exitosamente')
            return redirect('lista_productos')
    else:
        form = ProductoDañadoForm()
    return render(request, 'inventario/productos/mover_dañados.html', {'form': form, 'producto': producto})