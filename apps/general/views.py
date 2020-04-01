from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from apps.general.models import TipoDocumento
from apps.general.models import Moneda
from apps.general.forms import MonedaForm
from apps.general.forms import DocumentoForm
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
from apps.perfil.models import Perfil
from apps.cotizaciones.models import CotizacionCabecera
from apps.ordencompra.models import OrdenCabecera
from apps.cotizaciones.models import CuerpoCotizacion
from apps.cotizaciones.models import ItemPago
from apps.items.models import Producto

def changeforcepassword(request):
	usss = get_object_or_404(User, id = request.user.id)
	form = PasswordChangeForm(request.user, request.POST)
	if request.method=='POST':
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			Perfil.objects.filter(User=usss).update(ChangePass=True)
			messages.success(request, 'Contraseña cambiada SATISFACTORIAMENTE!')
			return redirect('dashboard')
	context = {"form":form}
	return render(request, 'registration/password_change_form.html',context)


# Create your views here.
def dashboard(request):
	qtn = CotizacionCabecera.objects.all()
	ventas = CotizacionCabecera.objects.all().order_by('-id')[:5]
	com = OrdenCabecera.objects.all()
	orden = OrdenCabecera.objects.all().order_by('-id')[:5]
	pro = Producto.objects.all().order_by('-id')[:5]
	conqnt=0
	conqtnfacturado=0
	conorden=0
	conorderealizado=0
	for q in qtn:
		conqnt = conqnt + 1
	for q in qtn:
		if q.Estado == 'FACTURADO':
			conqtnfacturado = conqtnfacturado + 1
	for o in com:
		conorden = conorden + 1
	for o in com:
		if o.Estado == 'FACTURADO':
			conorderealizado = conorderealizado + 1
	context = {"conqnt":conqnt,'conqtnfacturado':conqtnfacturado,'conorden':conorden,'conorderealizado':conorderealizado,'ventas':ventas,'orden':orden,'producto':pro}
	return render(request, "dashboard.html", context)

def detallemoneda(request):
	mon = Moneda.objects.all()
	context = {"Moneda":mon}
	return render(request, "generales/monedas.html", context)


def registrarmonedas(request):
	form = MonedaForm(request.POST or None)
	if(request.method=='POST'):
		formResult=form.save()
		if(form.is_valid()):
			form.save()
			return redirect('generales:detallemoneda')
	context = {'form':form}
	return render(request, 'generales/registrarmonedas.html', context)


def detalledocumento(request):
	doc = TipoDocumento.objects.all()
	context = {"TipoDocumento":doc}
	return render(request, "generales/documento.html", context)


def registrardocumento(request):
    form = DocumentoForm(request.POST or None)
    if(request.method=='POST'):
        formResult=form.save()
        if(form.is_valid()):
            form.save()
            return redirect('generales:detalledocumento')
    context = {'form':form}
    return render(request, 'generales/registrardoc.html', context)


def editarmoneda(request, id):
    mon = get_object_or_404(Moneda, id = id)
    form = MonedaForm(request.POST or None,request.FILES or None,instance=mon)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('generales:detallemoneda')
        else:
            return redirect('generales:registrarmonedas', id=id)
    context = {'form':form}
    return render(request, 'generales/registrarmonedas.html', context)


def Deletemoneda(request, id):
	mon = get_object_or_404(Moneda, id=id)
	aeliminar = ['Eliminar contacto','Realmente Desea eliminar el contacto <strong>{}</strong>?<br><strong><small>Esta acción no se puede deshacer</small></strong>'.format(str(mon.Moneda))]
	if request.method=='POST':
		Moneda.objects.filter(id=id).delete()
		messages.success(request, 'Se eliminó el profesional SATISFACTORIAMENTE.')
		return redirect('generales:detallemoneda')
	context = {"aeliminar":aeliminar, 'atras':request.META.get('HTTP_REFERER')}
	return render(request,'base/deleteform.html',context)


def editardocumento(request, id):
    tip = get_object_or_404(TipoDocumento, id = id)
    form = DocumentoForm(request.POST or None,request.FILES or None,instance=tip)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('generales:detalledocumento')
        else:
            return redirect('generales:registrardocumento', id=id)
    context = {'form':form}
    return render(request, 'generales/registrardoc.html', context)


def Deletedocumento(request, id):
	doc = get_object_or_404(TipoDocumento, id=id)
	aeliminar = ['Eliminar contacto','Realmente Desea eliminar el contacto <strong>{}</strong>?<br><strong><small>Esta acción no se puede deshacer</small></strong>'.format(str(doc.Name))]
	if request.method=='POST':
		TipoDocumento.objects.filter(id=id).delete()
		messages.success(request, 'Se eliminó el profesional SATISFACTORIAMENTE.')
		return redirect('generales:detalledocumento')
	context = {"aeliminar":aeliminar, 'atras':request.META.get('HTTP_REFERER')}
	return render(request,'base/deleteform.html',context)
