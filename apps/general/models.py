from django.db import models

# Create your models here.
class TipoDocumento(models.Model):
	Name = models.CharField("Tipo de Documento", max_length=200, default='')
	Abreviatura = models.CharField("Abreviatura", max_length=200, default='')

	class Meta:
		verbose_name = 'Tipo Documento'
		verbose_name_plural = 'Tipos Documento'

	def __str__(self):
		return "%s" % (self.Abreviatura)


class Moneda(models.Model):
	Moneda = models.CharField("Nombre Moneda", max_length=100, default='')
	Plural = models.CharField("Nombre Moneda Plural", max_length=100, default='')
	Signo = models.CharField("Signo", max_length=10, default='')
	Denominacion = models.CharField("Denominacion", max_length=5, default='')

	class Meta:
		verbose_name = "Moneda"
		verbose_name_plural = "Monedas"

	def __str__(self):
		return "%s" %(self.Moneda)
