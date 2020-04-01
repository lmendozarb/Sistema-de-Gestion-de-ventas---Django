from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth.decorators import login_required

from apps.cotizaciones.views import gestionaQTN
from apps.cotizaciones.views import cabeceracotizacion
from apps.cotizaciones.views import boucher
from apps.cotizaciones.views import RegistrarItem

from apps.cotizaciones.views import cambiarContacto
from apps.cotizaciones.views import RegistrarItem

from apps.cotizaciones.views import ConfirmCotizacion
from apps.cotizaciones.views import DeconfirmCotizacion
from apps.cotizaciones.views import AnulateCotizacion
from apps.cotizaciones.views import PagoUrl

from apps.cotizaciones.views import CotizacionPDF

urlpatterns = [
	path("detalle/",login_required(gestionaQTN),name="gestionaQTN"),
	path("registrar/",login_required(cabeceracotizacion),name="cabeceracotizacion"),
	path("boucher/<int:id>",login_required(boucher),name="boucher"),
	path('boucher/<int:id>/confirmar',login_required(ConfirmCotizacion), name="ConfirmCotizacion"),
	path('boucher/<int:id>/desconfirmar',login_required(DeconfirmCotizacion), name="DeconfirmCotizacion"),
	path('boucher/<int:id>>/anular',login_required(AnulateCotizacion), name="AnulateCotizacion"),
	path("boucher/<int:id>/item",login_required(RegistrarItem),name="RegistrarItem"),
	path("boucher/<int:id>/contacto/<int:idcont>",login_required(cambiarContacto),name="cambiarContacto"),
	path("boucher/<int:id>/item/<int:iditem>",login_required(RegistrarItem),name="RegistrarItem"),
	path("boucher/<int:id>/pagourl/<code>",login_required(PagoUrl),name="PagoUrl"),
	# path('processpayment/',ProcessPayment, name='processpayment'),
	path("exportar/<int:id>/",CotizacionPDF,name="CotizacionPDF"),




]
