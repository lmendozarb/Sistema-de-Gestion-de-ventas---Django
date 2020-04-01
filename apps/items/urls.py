from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth.decorators import login_required

from apps.items.views import DetalleProducto
from apps.items.views import RegistroProducto
from apps.items.views import EditarProducto
from apps.items.views import ElminarProducto





urlpatterns = [
	path("detalle/",login_required(DetalleProducto),name="DetalleProducto"),
	path("registro/",login_required(RegistroProducto),name="RegistroProducto"),
	path("editar/<int:id>",login_required(EditarProducto),name="EditarProducto"),
	path("editar/<int:id>/delete",login_required(ElminarProducto),name="ElminarProducto"),



]
