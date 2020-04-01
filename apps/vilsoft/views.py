from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages

from apps.vilsoft.models import DatosEmpresa
from apps.vilsoft.forms import EnterpriseDataForm

from apps.perfil.forms import PerfilUsuarioForm
from apps.perfil.models import Perfil
from django.contrib.auth.models import Group
from apps.vilsoft.forms import UserForm

from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils.html import strip_tags
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from weasyprint import HTML
from weasyprint.fonts import FontConfiguration
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from apps.vilsoft.forms import UserEditForm
# Create your views here.

def enterprisedata(request):
	enterprise = get_object_or_404(DatosEmpresa, id=1)
	form = EnterpriseDataForm(request.POST or None, instance = enterprise)
	if request.method=='POST':
		if form.is_valid():
			form.save()
			messages.success(request, 'Se editaron los datos de Vilsoft SATISFACTORIAMENTE.')
			return redirect('vilsoft:enterprisedata')
	context = {'form':form}
	return render(request, 'vilsoft/enterprise.html', context)

def detalleUsuarios(request):
	per = Perfil.objects.all()
	context = {"Perfil":per}
	return render(request, "usuarios/detalle.html", context)

def RegistrarUsuarios(request):
	grupos = Group.objects.all().order_by("-id")
	formProfile = PerfilUsuarioForm(request.POST,request.FILES or None)
	formUser = UserForm(request.POST,request.FILES or None)
	idgrup = request.POST.get('GroupPermission', 0)
	if request.method=='POST':
		if formUser.is_valid():
			if formProfile.is_valid():
				iduser = formUser.save(commit=False)
				username = request.POST.get('username', 0)
				iduser.set_password(username)
				iduser.save()
				idprofile = formProfile.save(commit = False)
				idprofile.User = iduser
				idprofile.save()
				group=Group.objects.get(id=idgrup)
				iduser.groups.add(group)
				html="vil/welcome.html"
				mensaje = "<p>El presente correo es para darle la bienvenida al sistema de Gestión de Vilsoft.</p> <p><br> <ul style='list-style:none;'><li><strong>Nivel de Acceso: </strong><span>{}</span><br><br></li><li><strong>Link Acceso: </strong><span><a style='color:#1d6f3d; text-decoration:none;' href='{}' target='_blank'>{}</a></span><br><br></li> <li><strong>Usuario:</strong> <span>{}</span> <br><br></li> <li><strong>Clave:</strong> <span>{}</span><br><br></li> </ul> </p> <p tyle='text-align:center;'><small>Al ingresar, deberá cambiar obligatoriamente su clave.</small></p>".format(group.name,"http://djangowebdemo.eastus.cloudapp.azure.com/","http://djangowebdemo.eastus.cloudapp.azure.com/",iduser.username,iduser.username)
				noms = "{} {}".format(iduser.first_name, iduser.last_name)
				SentMail("Bienvenido a VILSOFT", iduser.email, mensaje, noms, html)
				messages.success(request, 'Se creó el Usuario SATISFACTORIAMENTE.')
				return redirect('vilsoft:detalleUsuarios')
			else:
				print("ERROR2")
	context = {'form':formProfile,'form2':formUser,"grupos":grupos}
	return render(request, 'usuarios/registrarusuarios.html', context)


def EditarUsuarios(request, id):
	grupos = Group.objects.all().order_by("-id")
	idgrup = request.POST.get('GroupPermission', 0)
	per = get_object_or_404(Perfil, id = id)
	formProfile = PerfilUsuarioForm(request.POST or None,request.FILES or None,instance=per)
	formUser = UserEditForm(request.POST or None,request.FILES or None,instance=per.User)
	if request.method=='POST':
		if formUser.is_valid():
			if formProfile.is_valid():
				iduser = formUser.save(commit=False)
				iduser.save()
				idprofile = formProfile.save(commit = False)
				idprofile.User = iduser
				idprofile.save()
				group=Group.objects.get(id=idgrup)
				iduser.groups.add(group)
				messages.success(request, 'Se editó el Usuario SATISFACTORIAMENTE.')
				return redirect('vilsoft:detalleUsuarios')
			else:
				return redirect('vilsoft:EditarUsuarios', id=id)
	context = {'form':formProfile,'form2':formUser,"grupos":grupos}
	return render(request, 'usuarios/editarusuarios.html', context)


def EliminarUsuario(request, id):
	per = get_object_or_404(Perfil, id=id)
	aeliminar = ['Eliminar usuario','Realmente Desea eliminar el usuario <strong>{}</strong>?<br><strong><small>Esta acción no se puede deshacer</small></strong>'.format(str(per.User.first_name))]
	if request.method=='POST':
		Perfil.objects.filter(id=id).delete()
		messages.success(request, 'Se eliminó el Usuario SATISFACTORIAMENTE.')
		return redirect('vilsoft:detalleUsuarios')
	context = {"aeliminar":aeliminar, 'atras':request.META.get('HTTP_REFERER')}
	return render(request,'base/deleteform.html',context)


def SentMail(asunto, Correo, mensaje='',nombreusuario='',html=''):
	context = {"nombreusuario":nombreusuario,"contenido":mensaje}
	html_content = render_to_string(html, context)
	text_content = strip_tags(html_content)
	subject = asunto
	email_from = settings.EMAIL_HOST_USER
	recipient_list = [Correo,]
	msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
	msg.attach_alternative(html_content, "text/html")
	msg.send()
