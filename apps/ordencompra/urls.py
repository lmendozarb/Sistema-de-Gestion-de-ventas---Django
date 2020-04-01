from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from apps.ordencompra.views import DetalleCompra
from apps.ordencompra.views import CreateCompra
from apps.ordencompra.views import OrdenCompra
from apps.ordencompra.views import AnulateOrden
from apps.ordencompra.views import RegistrarItem
from apps.ordencompra.views import CierreOrden
from apps.ordencompra.views import OdenPDF


from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('detalle/',login_required(DetalleCompra), name='DetalleCompra'),
	path('registrar/',login_required(CreateCompra), name='CreateCompra'),
	path('Orden/<int:id>',login_required(OrdenCompra), name='OrdenCompra'),
	path('Orden/<int:id>/anular',login_required(AnulateOrden), name="AnulateOrden"),
	path('Orden/<int:id>/producto/<int:iditem>',login_required(RegistrarItem), name="RegistrarItem"),
	path('Orden/<int:id>/generar',login_required(CierreOrden), name='CierreOrden'),
	path('Orden/<int:id>/exportar',login_required(OdenPDF), name='OdenPDF'),

	]
