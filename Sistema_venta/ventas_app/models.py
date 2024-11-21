from typing import Iterable
from django.db import models
from .choices import CATEGORIAS 
from django.core.validators import MinValueValidator,MaxValueValidator,MaxLengthValidator,MinLengthValidator
from .validadores import validacion_numeros
# Create your models here.
class Clientes (models.Model):
    cedula = models.CharField(max_length=10,primary_key=True,unique=True,validators=[MinLengthValidator(10),validacion_numeros])
    nombre = models.CharField(max_length=50,blank=False,verbose_name= 'Nombre del cliente')
    apellido = models.CharField(max_length=50,blank=False)
    telefone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f" {self.cedula} {self.nombre} {self.apellido} "
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'Clientes'

class Productos(models.Model):
        codigo = models.CharField(max_length=10, primary_key=True, unique=True)
        nombre = models.CharField(max_length=50, blank=False, verbose_name= 'Nombre del producto')
        marca = models.CharField(max_length=50,unique=True)
        caracteristicas_categoria = models.CharField(max_length=100,choices= CATEGORIAS)
        precio = models.DecimalField(max_digits=10, decimal_places=2, help_text='Ingresa valores con decimales', verbose_name='Precio del producto')
        cantidad_stock = models.IntegerField(verbose_name='Cantidad en stock')
        fecha_ingreso = models.DateTimeField(auto_now_add=True)
        fecha_elaboracion = models.DateField()
        fecha_vencimiento = models.DateField()

        def actualizar_stock (self, cantidad):
            self.cantidad_stock = self.cantidad_stock - cantidad
            self.save() #metodo propio que me ofrece django 

        def __str__(self):
            return f"{self.nombre}' ' {self.marca} "
        class Meta:
            verbose_name = 'Producto: '
            verbose_name_plural = 'Productos: '
            db_table = 'Productos'


class Empresas (models.Model):
        ruc = models.CharField(max_length=13, primary_key=True, unique=True)
        nombre = models.CharField(max_length=50, blank=False, verbose_name= 'Nombre de la empresa')
        direccion = models.CharField(max_length=50)
        telefono = models.CharField(max_length=10)
        email = models.EmailField(unique=True)
        def __str__(self):
            return f"{self.nombre} "
        class Meta:
             verbose_name = 'Empresa'
             verbose_name_plural = 'Empresas'
             db_table = 'Empresas'

class Proveedores (models.Model):
     cedula = models.CharField(max_length=10, primary_key=True, unique=True, validators=[MinLengthValidator(10)])
     nombre = models.CharField(max_length=50, blank=False,verbose_name='Nombre del proveedor')
     apellido = models.CharField(max_length=50, blank=False)
     telefone = models.CharField(max_length=10)
     email = models.EmailField(unique=True)
     empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE) 

     def __str__(self):
          return f"{self.nombre} {self.apellido} "
     class Meta:
          verbose_name = 'Proveedor'
          verbose_name_plural = 'Proveedores'
          db_table = 'Proveedores'

class Empleado(models.Model):
     cedula = models.CharField(max_length=10, primary_key=True, unique=True, validators=[MinLengthValidator(10)],verbose_name='Cedula Empleado')
     nombre = models.CharField(max_length=50, blank=False, verbose_name='Nombre del empleado')
     apellido = models.CharField(max_length=50, blank=False)
     telefone = models.CharField(max_length=10)
     email = models.EmailField(unique=True)
     direccion = models.TextField()
     fecha_creacion = models.DateTimeField(auto_now_add=True)
     fecha_nacimiento = models.DateField()

     def __str__(self):
          return f"{self.nombre} {self.apellido} "
     class Meta:
          verbose_name = 'Empleado'
          verbose_name_plural = 'Empleados'
          db_table = 'Empleados'

from decimal import Decimal

class Facturas (models.Model):
     codigo_factura = models.AutoField(primary_key=True)
     fecha_factura = models.DateTimeField(auto_now_add=True)
     cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
     empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
     producto = models.ForeignKey(Productos,on_delete=models.CASCADE)
     cantidad = models.IntegerField()
     subtotal = models.DecimalField(max_digits=10,decimal_places=2,editable=True,default=0)
     iva = models.DecimalField(max_digits=10, decimal_places=2,editable=True,default=0)
     total = models.DecimalField(max_digits=10, decimal_places=2, editable=False,default=0)

     def save(self,*args,**kwargs):# acceder el self hace referencia a los campos del modelo, args a los argumentos que tiene ese modelo
          self.subtotal = self.producto.precio * self.cantidad
          self.iva = self.subtotal * Decimal(0.15)
          self.total = self.subtotal + self.iva
          self.producto.cantidad_stock = int(self.producto.cantidad_stock)- int(self.cantidad)
          self.producto.actualizar_stock()
          super().save(*args,**kwargs)
    
     def __str__(self):
          return f"Factura {self.codigo_factura} del cliente {self.cliente} con un total de {self.total}"

     class Meta:
      verbose_name = 'Factura'
      verbose_name_plural = 'Facturas'
      db_table = 'Facturas'
#paso 1 vamos a irnos a la aplicacion en nuevo archivo y creamos un nuevo modulo y le ponemos choice.py