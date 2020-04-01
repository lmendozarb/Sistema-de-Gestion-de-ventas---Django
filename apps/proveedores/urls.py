from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth.decorators import login_required


from apps.proveedores.views import DetalleProveedor
from apps.proveedores.views import RegistrarProveedores
from apps.proveedores.views import EditarProveedores
from apps.proveedores.views import DeleteProveedor
urlpatterns = [

	path("detalle/",login_required(DetalleProveedor),name="DetalleProveedor"),
	path("registrar/",login_required(RegistrarProveedores),name="RegistrarProveedores"),
	path("editar/<int:id>",login_required(EditarProveedores),name="EditarProveedores"),
	path("editar/<int:id>/delete",login_required(DeleteProveedor),name="DeleteProveedor"),


]
