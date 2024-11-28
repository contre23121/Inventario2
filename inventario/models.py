from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Proveedor(models.Model):
    proveedorid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, null=True)
    telefono = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    categoriaid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    productoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_por_caja = models.IntegerField(default=0)
    cantidad_por_unidad = models.IntegerField(default=0)
    categoriaid = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    proveedorid = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre

class ProductosVencidos(models.Model):
    productovencidoid = models.AutoField(primary_key=True)
    productoid = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_vencimiento = models.DateTimeField()
    cantidad = models.IntegerField()

class ProductosDañados(models.Model):
    productodañadoid = models.AutoField(primary_key=True)
    productoid = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_reporte = models.DateTimeField()
    cantidad = models.IntegerField()
    descripcion = models.CharField(max_length=255)

class HistorialInventario(models.Model):
    historialid = models.AutoField(primary_key=True)
    productoid = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField()
    tipo_movimiento = models.CharField(max_length=50)
    usuarioid = models.ForeignKey(User, on_delete=models.CASCADE)

class HistorialTransferenciasDROPS(models.Model):
    transferenciaid = models.AutoField(primary_key=True)
    productoid = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_transferencia = models.DateTimeField()
    tipo_transferencia = models.CharField(max_length=50)
    usuarioid = models.ForeignKey(User, on_delete=models.CASCADE)