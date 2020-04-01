from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth.decorators import login_required
from apps.general.views import detallemoneda
from apps.general.views import registrarmonedas
from apps.general.views import editarmoneda
from apps.general.views import Deletemoneda
from apps.general.views import detalledocumento
from apps.general.views import registrardocumento
from apps.general.views import editardocumento
from apps.general.views import Deletedocumento





urlpatterns = [


	path("monedas/",login_required(detallemoneda),name="detallemoneda"),
	path("moneda/registrar/",login_required(registrarmonedas),name="registrarmonedas"),
	path("docindentidad/",login_required(detalledocumento),name="detalledocumento"),
	path("docidentidad/redistrar/",login_required(registrardocumento),name="registrardocumento"),
	path("moneda/editar/<int:id>", login_required(editarmoneda), name="editarmoneda"),
	path("moneda/<int:id>/delete", login_required(Deletemoneda), name="Deletemoneda"),
	path("docindentidad/editar/<int:id>", login_required(editardocumento), name="editardocumento"),
	path("docindentidad/<int:id>/delete", login_required(Deletedocumento), name="Deletedocumento"),
	

]
