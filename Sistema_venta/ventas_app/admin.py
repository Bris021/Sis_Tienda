from django.contrib import admin
from .models import Clientes,Productos,Empresas,Proveedores,Empleado,Facturas
# Register your models here.
admin.site.register(Clientes)
admin.site.register(Productos)
admin.site.register(Empresas)
admin.site.register(Proveedores)
admin.site.register(Facturas)
admin.site.register(Empleado)


