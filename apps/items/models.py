from django.db import models
from apps.proveedores.models import Proveedor

# Create your models here.
class Producto(models.Model):
	TYPE_PRODUCT = (
		(0,'Hardware'),
		(1,'Software')
	)
	SerializeProducto = models.IntegerField("Nro. de Producto", default=0)
	Nombre = models.CharField("Nombre del Producto", max_length=200)
	Foto = models.ImageField('Foto', upload_to="Items", blank=True, null=True ,default='/non/newitem.jpg')
	TipoProducto = models.IntegerField('Tipo del Producto',choices=TYPE_PRODUCT, default=2)
	Descripcion = models.TextField("Descripción",null=True, blank=True)
	Precio = models.DecimalField("Precio de Venta", blank=True, null=True, max_digits=10, default=0.0,decimal_places=2)
	PrecioCompra = models.DecimalField("Precio de Compra", blank=True, null=True, max_digits=10, default=0.0,decimal_places=2)
	Cantidad = models.IntegerField("Cantidad", blank=True, null=True, default=0 )
	FechaRegistro = models.DateTimeField(auto_now=True)
	ProveedorItem = models.ForeignKey(Proveedor, on_delete=models.CASCADE,null=True, blank=True)

	class Meta:
		verbose_name = 'Producto'
		verbose_name_plural = 'Productos'

	def __str__(self):
		return "PR.%s" % (str(self.SerializeProducto).zfill(4))
