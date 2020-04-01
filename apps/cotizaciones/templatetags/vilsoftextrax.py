from django import template
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from decimal import Decimal
from apps.cotizaciones.models import CotizacionCabecera
from apps.ordencompra.models import OrdenCabecera
register = template.Library()

@register.simple_tag()
def calcularigvODE(id,subtotal, *args, **kwargs):
	compra= OrdenCabecera.objects.get(id=id)
	igv = subtotal * Decimal('0.18')
	return round(igv, 2)



@register.simple_tag()
def calculartotalODE(id,subtotal,  *args, **kwargs):
	compra= OrdenCabecera.objects.get(id=id)
	igv = subtotal * Decimal('1.18')
	return round(igv, 2)

@register.simple_tag()
def calcularigv(id,subtotal, *args, **kwargs):
	cabe = get_object_or_404(CotizacionCabecera, id = id)
	descuento = cabe.Descuento
	igv = (subtotal-descuento) * Decimal('0.18')
	return round(igv, 2)



@register.simple_tag()
def calculartotal(id,subtotal,  *args, **kwargs):
	cabe = get_object_or_404(CotizacionCabecera, id = id)
	descuento = cabe.Descuento
	igv = (subtotal-descuento) * Decimal('1.18')
	return round(igv, 2)


@register.simple_tag()
def multiproducto(cantidad,precio ,  *args, **kwargs):
	total = cantidad*precio
	return round(total, 2)


@register.filter(name='has_group')
def has_group(user, group_name):
	return user.groups.filter(name=group_name).exists()

@register.simple_tag()
def groupsnamesfromuser(id, *args, **kwargs):
	ugru = ""
	uss  = get_object_or_404(User, id=id)
	usergrup = uss.groups.all()
	nouser = ""

	for a in usergrup:
		if len(nouser) == 0:
			nouser = a
		else:
			nouser = "{},{}".format(nouser, a)

	return nouser

@register.simple_tag()
def backgroundbooking(Estado):
	if Estado == "COTIZACIÓN":
		return "background-color: #ffffff;"
	elif Estado == "CONFIRMAR":
		return "background-color: #fff1b9;"
	elif Estado == "ANULAR":
		return "background-color: #ffc2c2;"
	elif Estado == "FACTURADO":
		return "background-color: #bdffd1;"

@register.simple_tag()
def fontcolor(Estado):
	if Estado == "COTIZACIÓN":
		return "color: #8392a5;"
	elif Estado == "CONFIRMAR":
		return "color: #69b2f8;"
	elif Estado == "ANULAR":
		return "color: #dc3545;"
	elif Estado == "FACTURADO":
		return "color: #10b759;"

@register.simple_tag()
def icono(Estado):
	if Estado == "COTIZACIÓN":
		return "icon ion-md-checkmark"
	elif Estado == "CONFIRMAR":
		return "icon ion-md-checkmark"
	elif Estado == "ANULAR":
		return "icon ion-md-close"
	elif Estado == "FACTURADO":
		return "icon ion-md-checkmark"
