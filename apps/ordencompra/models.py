from django.db import models
from apps.proveedores.models import Proveedor
from apps.items.models import Producto
# Create your models here.
class OrdenCabecera(models.Model):
	CONDICION_CHOICES = (
		('CONTADO','CONTADO'),
		('CREDITO','CREDITO'),
		('CREDITO Y CONTADO','CREDITO Y CONTADO')
	)
	STATE_CHOICES = (
		('CONFIRMAR','CONFIRMAR'),
		('FACTURADO','FACTURADO'),
		('ANULAR','ANULAR'),
	)
	ContSerializeQtn = models.IntegerField("Nro. Cotización", default=0)
	SerializeQtn = models.IntegerField("Versión Cotización", default=0)
	FechaCreacion = models.DateTimeField("Fecha de Creación", auto_now_add=True, blank=True)
	CondicionVenta = models.CharField(choices = CONDICION_CHOICES, default='CONFIRMAR',max_length=50)
	Proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	Estado = models.CharField('Estado', max_length=20,choices=STATE_CHOICES)

	class Meta:
		verbose_name = 'Orden de Compra'
		verbose_name_plural = 'Orden de Compra'

	def __str__(self):
		return "ODE.%s.%s.%s" % (self.FechaCreacion.year,str(self.ContSerializeQtn).zfill(4),str(self.SerializeQtn).zfill(2))


class OrdenCompraBody(models.Model):
	Item = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)
	Cantidad = models.IntegerField("Cantidad", blank=True, null=True )
	CompraHead = models.ForeignKey(OrdenCabecera, on_delete=models.CASCADE, null=True, blank=True)

	class Meta:
		verbose_name = 'CompraBody'
		verbose_name_plural = 'ComprasBody'

	def __str__(self):
		return "%s" % (self.Item)

class OrdenCompraCierre(models.Model):
	FacturaCompraFisico = models.FileField('Factura Fisico', upload_to="Facturas/", default='/non/non.jpg')
	GuiadeRemisionFisico = models.FileField('Guia de Remisión Fisico', upload_to="guias/",default='/non/non.jpg')
	CompraHead = models.ForeignKey(OrdenCabecera, on_delete=models.CASCADE, null=True, blank=True)
	class Meta:
		verbose_name = 'CompraCierre'
		verbose_name_plural = 'CompraCierre'

	def __str__(self):
		return "%s" % (self.CompraHead)
