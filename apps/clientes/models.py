from django.db import models
from apps.general.models import TipoDocumento

# Create your models here.
class Contacto(models.Model):
	NombreContacto = models.CharField("Nombres Contacto Cliente", max_length=255, default="")
	ApellidoContacto = models.CharField("Apellidos Contacto Cliente", max_length=255, default="")
	TipoDocumentoContacto = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE,related_name="TipoDocumentoContacto", blank=True, null=True)
	NroDocumentoContacto = models.CharField("Número Documento", max_length=50, blank=True, null=True, default="")
	CorreoElectronicoContacto = models.CharField("Correo Electrónico", max_length=300)
	MovilContacto = models.CharField("Teléfono Móvil", max_length=20)
	LugarTrabajo = models.CharField("Lugar de Trabajo", max_length=20, default="")
	Cargo = models.CharField("Cargo", max_length=20, blank=True, null=True, default="")
	Principal = models.BooleanField("Contacto Principal", default=False)

	class Meta:
		verbose_name = 'Contacto de Cliente'
		verbose_name_plural = 'Contactos de Clientes'

	def __str__(self):
		return "%s %s" % (self.NombreContacto, self.ApellidoContacto)



class Clientes(models.Model):
	STATUS_CHOICES = (
		(1, "Persona Jurídica"),
		(2, "Persona Natural con Negocio"),
		(3, "Persona Natural sin Negocio")
	)
	RazonSocial = models.CharField("Razón Social", max_length=100, default="")
	Website = models.URLField("WebSite", blank=True, null=True)
	CorreoElectronico = models.EmailField("Correo Electrónico", max_length=500, blank=True, null=True)
	TipoPersona = models.IntegerField(choices=STATUS_CHOICES)
	RUC = models.CharField("RUC", max_length=15)
	DireccionLegal = models.CharField("Dirección Legal", max_length=500)
	LegalName = models.CharField("Nombres Representante Legal", max_length=255, default="", blank=True, null=True)
	LegalLastName = models.CharField("Apellidos Representante Legal", max_length=255, default="", blank=True, null=True)
	TipoDocumentoLegal = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, related_name="TipoDocumentoLegal", blank=True, null=True)
	NroDocumentoLegal = models.CharField("Número Documento", max_length=50, blank=True, null=True, default="")
	ContactoClientes =  models.ManyToManyField(Contacto)

	class Meta:
		verbose_name = 'Cliente'
		verbose_name_plural = 'Clientes'

	def __str__(self):
		return "%s" % (self.RazonSocial)
