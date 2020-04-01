from django.db import models

# Create your models here.
class DatosEmpresa(models.Model):
	Nombre = models.CharField("Razón Social", max_length = 200)
	NickName = models.CharField("Nombre Comercial", max_length = 200)
	Direccion = models.CharField("Dirección", max_length = 500)
	Website = models.CharField("Website", max_length = 300)
	Mail = models.EmailField("Correo Electrónico", max_length = 300)
	RUC = models.CharField("RUC", max_length = 30)
	Telefono = models.CharField("Telefono", max_length = 30,default="")


	class Meta:
		verbose_name = 'Datos de la Empresa'
		verbose_name_plural = 'Datos de la Empresa'

	def __str__(self):
		return "%s" % (self.NickName)
