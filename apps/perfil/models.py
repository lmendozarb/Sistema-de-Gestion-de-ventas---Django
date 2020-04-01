from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Perfil(models.Model):
	User = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
	Foto = models.ImageField('Foto', upload_to="Perfil", blank=True, null=True ,default='/non/images.png')
	movil = models.CharField("Movil", max_length=20, default='')
	ChangePass = models.BooleanField("Clave Cambiada", default = False)

	class Meta:
		verbose_name = "Perfil"
		verbose_name_plural = "Perfiles"

	def __str__(self):
		return "%s" % (self.User)
