from django.db import models
from apps.general.models import Moneda
from apps.clientes.models import Clientes
from apps.items.models import Producto
from apps.proveedores.models import Proveedor


# Create your models here.
class CotizacionCabecera(models.Model):
	STATE_CHOICES = (
		('COTIZACIÓN','COTIZACIÓN'),
		('CONFIRMAR','CONFIRMAR'),
		('FACTURADO','FACTURADO'),
		('ANULAR','ANULAR'),
	)
	ContSerializeQtn = models.IntegerField("Nro. Cotización", default=0)
	SerializeQtn = models.IntegerField("Versión Cotización", default=0)
	FechaCreacion = models.DateTimeField("Fecha de Creación", auto_now_add=True, blank=True)
	Cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, blank=True, null=True)
	# Vendedor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	Moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
	TiempoEntrega = models.CharField("Tiempo de Entrega", max_length=200, blank=True, null=True)
	Asunto = models.CharField("Asunto de la Cotizacion",max_length=200)
	Estado = models.CharField('Estado', max_length=15,choices=STATE_CHOICES)
	Descripcion = models.TextField("Descripción",null=True, blank=True)
	Descuento = models.DecimalField("Descuento", max_digits=10, default=0.0,decimal_places=2,null=True, blank=True)
	FechaRegistro = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Cotización'
		verbose_name_plural = 'Cotización'

	def __str__(self):
		return "VLF.%s.%s.%s" % (self.FechaCreacion.year,str(self.ContSerializeQtn).zfill(4),str(self.SerializeQtn).zfill(2))


class CuerpoCotizacion(models.Model):
	cabecera = models.ForeignKey(CotizacionCabecera, on_delete=models.CASCADE, blank=True, null=True)
	item = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True)
	cantidad = models.IntegerField("Cantidad", blank=True, null=True )
	precio = models.DecimalField("Precio", blank=True, null=True, max_digits=10, default=0.0,decimal_places=2)

	class Meta:
		verbose_name = 'Cuerpo Cotizacion'
		verbose_name_plural = 'Cuerpo de Cotizacion'


class ItemPago(models.Model):
	cabecera = models.ForeignKey(CotizacionCabecera, on_delete=models.CASCADE, blank=True, null=True)
	NombrePago = models.CharField("Nombre del Pago", max_length=500, default='')
	FechaRegistro = models.DateTimeField("Fecha de Registro", auto_now_add=True, blank=True)
	NroPago = models.CharField("Número de Pago", max_length=20)
	Estado = models.BooleanField("Estado del Item", default=False)
	CodigoReferencia = models.CharField("Código de Referencia", max_length=200,null=True, blank=True)
	NroTarjeta = models.CharField("Últimos dígitos de la tarjeta", max_length=30,null=True, blank=True)
	FechaPago = models.DateTimeField("Fecha de Pago",null=True, blank=True)
	Monto =  models.FloatField("Monto",null=False, default=0.0)
	EstadoPago = models.BooleanField("Estado del Pago", default=False)
	CodigoPublico  = models.CharField("Código Público", max_length=128)
	Cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, null=True)
	CulqiStatus = models.CharField("Código de Estado",default='', max_length=500)
	CulqiMessage = models.CharField("Mensaje de Pago", max_length=1000, default='')
	CulqiRefCode = models.CharField("Código Referencia Culqi", max_length=500, default='')
	CulqiAuthCode = models.CharField("Código de Autorización Culqi", max_length=500, default='')
	CulqiFee = models.FloatField("Comision Culqi", null = False, default=0.0)
	CulqiFeeTaxes = models.FloatField("Impuesto Comision Culqi ", null = False, default=0.0)

	class Meta:
		verbose_name = 'Pago Url'
		verbose_name_plural = 'Pago Url'

	def __str__(self):
		return "%s -> %s" % (self.NombrePago, self.FechaRegistro.strftime("%d/%m/%Y %H:%M:%S"))
