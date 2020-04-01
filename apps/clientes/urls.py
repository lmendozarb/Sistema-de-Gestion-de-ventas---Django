from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth.decorators import login_required


from apps.clientes.views import detallecliente
from apps.clientes.views import registrarclientes
from apps.clientes.views import editarclientes
from apps.clientes.views import registrarcontactos
from apps.clientes.views import editarcontactos
from apps.clientes.views import deletecontactos
from apps.clientes.views import Deleteclientes

urlpatterns = [
	path("detalle/",login_required(detallecliente),name="detallecliente"),
	path("registro/",login_required(registrarclientes),name="registrarclientes"),
	path("editar/<int:id>", login_required(editarclientes), name="editarclientes"),
	path("editar/<int:id>/nuevocontacto", login_required(registrarcontactos), name="registrarcontactos"),
	path("editar/<int:id>/editarcontacto/<int:idcont>/", login_required(editarcontactos), name="editarcontactos"),
	path("editar/<int:id>/eliminarcontacto/<int:idcont>/", login_required(deletecontactos), name="deletecontactos"),
	path("editar/<int:id>/eliminar", login_required(Deleteclientes), name="Deleteclientes"),



]
