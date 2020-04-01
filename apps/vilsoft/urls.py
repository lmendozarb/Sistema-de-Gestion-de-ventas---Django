from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth.decorators import login_required


from apps.vilsoft.views import enterprisedata
from apps.vilsoft.views import detalleUsuarios
from apps.vilsoft.views import RegistrarUsuarios
from apps.vilsoft.views import EditarUsuarios
from apps.vilsoft.views import EliminarUsuario

urlpatterns = [

	path('datosempresa/',login_required(enterprisedata), name="enterprisedata"),
	path("usuarios/", login_required(detalleUsuarios), name="detalleUsuarios"),
	path("usuarios/registrar/", login_required(RegistrarUsuarios), name="RegistrarUsuarios"),
	path("usuarios/editar/<int:id>", login_required(EditarUsuarios), name="EditarUsuarios"),
	path("usuarios/<int:id>/eliminar/", login_required(EliminarUsuario), name="EliminarUsuario"),


]
