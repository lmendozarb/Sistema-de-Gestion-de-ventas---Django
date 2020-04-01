from django.db import models
from apps.general.models import TipoDocumento
# Create your models here.

class Proveedor(models.Model):
	RazonSocial = models.CharField("Razón Social", max_length=100, default="")
	RUC = models.CharField("RUC", max_length=15)
	DireccionLegal = models.CharField("Dirección Legal", max_length=500)
	NombreContacto = models.CharField("Nombred del Contacto", max_length=255, default="")
	ApellidoContacto = models.CharField("Apellidos del Contacto", max_length=255, default="")
	TipoDocumentoProveedor = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, related_name="TipoDocumentoProveedor", blank=True, null=True)
	NroDocumentoProveeedor = models.CharField("Número Documento", max_length=50, blank=True, null=True, default="")
	CorreoElectronico = models.EmailField("Correo Electrónico", max_length=500)
	Movil = models.CharField("Celular", max_length=9,default="")

	class Meta:
		verbose_name = 'Proveedores'
		verbose_name_plural = 'Proveedores'

	def __str__(self):
		return "%s" % (self.RazonSocial)
