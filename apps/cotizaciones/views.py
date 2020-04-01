from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages

from apps.cotizaciones.models import CotizacionCabecera
from apps.cotizaciones.forms import QtnForm
from apps.cotizaciones.forms import DescuentoForm
from apps.cotizaciones.forms import CuerpoCotizacionForm
from apps.cotizaciones.models import CuerpoCotizacion
from apps.clientes.models import Clientes
from apps.cotizaciones.forms import QtnEditForm
from apps.clientes.forms import ContactoForm
from apps.clientes.models import Contacto

from apps.items.models import Producto
from django.http import JsonResponse
from django.template.loader import render_to_string
from apps.cotizaciones.models import ItemPago
from apps.vilsoft.models import DatosEmpresa

from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils.html import strip_tags
from django.utils.text import slugify
import hashlib
import smtplib
from datetime import datetime, date, time, timedelta
import culqipy
from decimal import Decimal
# Create your views here.
def gestionaQTN(request):
	qtn = CotizacionCabecera.objects.all().order_by('-id')
	context = {"CotizacionCabecera":qtn}
	return render(request, "cotizacion/detalle.html", context)


def boucher(request, id):
	bou = get_object_or_404(CotizacionCabecera, id=id)
	cuerpo = CuerpoCotizacion.objects.filter(cabecera=bou)
	pro = Producto.objects.all()
	formcon = ContactoForm(request.POST or None)
	if request.method=='POST':
		if formcon.is_valid():
			formResult=formcon.save()
			con = Contacto(formResult)
			resform = formcon.save(commit=False)
			resform.Principal = True
			resform.save()
			cli = get_object_or_404(Clientes, id = bou.Cliente.id)
			cli.ContactoClientes.add(con.id)
			for prin in bou.Cliente.ContactoClientes.all():
				if prin.Principal is True:
					prin.Principal = False
					prin.save()
					return redirect('cotizaciones:boucher', bou.id)

	formqnt = QtnEditForm(request.POST or None,request.FILES or None,instance=bou)
	if request.method == 'POST':
		if formqnt.is_valid():
			formqnt.save()
			return redirect('cotizaciones:boucher', bou.id)

	form = DescuentoForm(request.POST or None,request.FILES or None,instance=bou)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('cotizaciones:boucher', bou.id)

	sum = 0
	for a in cuerpo:
		total=a.precio*a.cantidad
		sum = sum + total

	tr="VLF.%s.%s.%s" % (bou.FechaCreacion.year,str(bou.ContSerializeQtn).zfill(4),str(bou.SerializeQtn).zfill(2))
	h = hashlib.sha512(tr.encode())
	sh=h.hexdigest()
	context = {'Producto':pro,'cuerpo':cuerpo,'formcon':formcon,'formqnt':formqnt,'form':form,"bou":bou,"id":id,"subtotal":sum,"code":sh}
	return render(request, "cotizacion/boucher.html", context)

def cabeceracotizacion(request):
	cliente = Clientes.objects.all()
	form = QtnForm(request.POST or None)
	if request.method=='POST':
		formResult=form.save()
		if form.is_valid() :
			formResult = form.save(commit=False)
			cliente = request.POST.get('Cliente', None)
			cli = cliente.split("-")
			clien = Clientes.objects.get(id=cli[0])
			formResult.Cliente = clien
			bf = CotizacionCabecera.objects.all().order_by("-ContSerializeQtn")[0]
			corr = bf.ContSerializeQtn + 1
			formResult.ContSerializeQtn = corr
			formResult.Estado="COTIZACIÓN"
			formResult.save()
			messages.success(request, 'Se registró la cotizacion SATISFACTORIAMENTE.')
			return redirect('cotizaciones:boucher',id=formResult.id)
	context = {'form':form,"cliente":cliente}
	return render(request, 'cotizacion/cabecera.html', context)


def cambiarContacto(request,id,idcont):
	bou = get_object_or_404(CotizacionCabecera, id=id)
	contacto = get_object_or_404(Contacto, id=idcont)
	for prin in bou.Cliente.ContactoClientes.all():
		if contacto.Principal is False and prin.Principal is True:
			contacto.Principal = True
			prin.Principal = False
			contacto.save()
			prin.save()
			return redirect('cotizaciones:boucher', bou.id)


def save_all(request,form,template_name,id,iditem):
	data = dict()
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			data['form_is_valid'] = True
			pro = Producto.objects.all()
			data['boucher'] = render_to_string('itemlist2.html',{'Producto':pro})
		else:
			data['form_is_valid'] = False
	context = {'form':form,"id":id,"iditem":iditem}
	data['html_form'] = render_to_string(template_name,context,request=request)
	return JsonResponse(data)


# def RegistrarItem2(request, id, iditem):
# 	form = CuerpoCotizacionForm(request.POST or None)
# 	if(request.method=='POST'):
# 		formResult=form.save()
# 		if(form.is_valid()):
# 			frore = form.save(commit=False)
# 			cabe = get_object_or_404(CotizacionCabecera,id=id)
# 			frore.cabecera = cabe
# 			produc = get_object_or_404(Producto,id=iditem)
# 			frore.item = produc
# 			frore.precio=produc.Precio
# 			frore.save()
# 			return redirect('cotizaciones:boucher',id=id)
# 	return save_all(request,form,'cotizacion/item2.html',id,iditem)
#
#
# def RegistrarItem2(request, id, iditem):
# 	form = CuerpoCotizacionForm(request.POST or None)
# 	if(request.method=='POST'):
# 		formResult=form.save()
# 		if(form.is_valid()):
# 			frore = form.save(commit=False)
# 			cabe = get_object_or_404(CotizacionCabecera,id=id)
# 			frore.cabecera = cabe
# 			produc = get_object_or_404(Producto,id=iditem)
# 			frore.item = produc
# 			frore.precio=produc.Precio
# 			frore.save()
# 			return redirect('cotizaciones:boucher',id=id)
# 	context = {'form':form,"id":id,"iditem":iditem}
# 	return render(request, 'cotizacion/cabecera.html', context)


def RegistrarItem(request, id, iditem):
	form = CuerpoCotizacionForm(request.POST or None)
	if(request.method=='POST'):
		formResult=form.save()
		if(form.is_valid()):
			frore = form.save(commit=False)
			cabe = get_object_or_404(CotizacionCabecera,id=id)
			frore.cabecera = cabe
			produc = get_object_or_404(Producto,id=iditem)
			frore.item = produc
			frore.precio=produc.Precio
			frore.save()
			return redirect('cotizaciones:boucher',id=id)
	context = {'form':form,"id":id,"iditem":iditem}
	return render(request, 'cotizacion/registraritem.html', context)


def ConfirmCotizacion(request, id):
	if request.user.is_superuser or request.user.groups.filter(name="Administrador").exists():
		cabe = CotizacionCabecera.objects.filter(id=id).update(Estado="CONFIRMAR")
		messages.success(request, 'Se confirmó la cotización SATISFACTORIAMENTE.')
		return redirect('cotizaciones:boucher', id)


def DeconfirmCotizacion(request, id):
	if request.user.is_superuser or request.user.groups.filter(name="Administrador").exists():
		cabe = CotizacionCabecera.objects.filter(id=id).update(Estado="COTIZACIÓN")
		messages.success(request, 'Se desconfirmó la cotización SATISFACTORIAMENTE.')
		return redirect('cotizaciones:boucher', id)


def AnulateCotizacion(request, id):
	if request.user.is_superuser or request.user.groups.filter(name="Administrador").exists():
		cabe = CotizacionCabecera.objects.filter(id=id).update(Estado="ANULAR")
		messages.success(request, 'Se Anuló la cotización SATISFACTORIAMENTE.')
		return redirect('cotizaciones:boucher', id)

def PagoUrl(request,id , code):
	cabe = get_object_or_404(CotizacionCabecera,id=id)
	cuerpo = CuerpoCotizacion.objects.filter(cabecera=cabe)
	vil = DatosEmpresa.objects.all()
	sum = 0
	for a in cuerpo:
		total=a.precio*a.cantidad
		sum = sum + total
	total = (sum-cabe.Descuento) * Decimal('1.18')
	if ItemPago.objects.filter(cabecera=cabe).exists():
		ItemPago.objects.filter(cabecera=cabe).update(Monto=total)
	else:
		ItemPago.objects.create(cabecera=cabe,CodigoPublico=code,Estado=False,NombrePago=cabe,Monto=total,Cliente=cabe.Cliente)

	pu=ItemPago.objects.get(cabecera=cabe)
	if pu.EstadoPago :
		CotizacionCabecera.objects.filter(id=id).update(Estado="FACTURADO")

	if cabe.Estado == 'FACTURADO':
		for c in cuerpo:
			it = Producto.objects.filter(id=c.item.id)
			for i in it:
				if c.item.id == i.id:
					resta = i.Cantidad - c.cantidad
					Producto.objects.filter(id=i.id).update(Cantidad=resta)
	question = get_object_or_404(ItemPago, CodigoPublico=code)
	context = {"id":id,"code":code,'cabe':cabe,'subtotal':sum,'total':total,'item': question,'vilsoft':vil,'pu':pu}
	return render(request, 'cotizacion/hlpu.html', context)


def ProcessPayment(request):
	if request.method == 'POST':
		server = smtplib.SMTP('smtp.gmail.com:587')
		token = request.POST['token']
		mail = request.POST['mail']
		denomination = request.POST['denomination']
		amount = int(float(request.POST['amount'].replace(",","."))*100)
		CodigoPublico = request.POST['CodigoPublico']
		culqipy.secret_key = "sk_test_nGczFokyhuLRVaRj"
		dir_charge = {'amount': amount,
					'capture': True,
					'currency_code': 'PEN',
					'description': denomination,
					'email': mail,
					'installments': 0,
					'metadata': {'order_id': '1234'},
					'source_id': token}
		charge = culqipy.Charge.create(dir_charge)
		if charge['object'] == "charge":
			oc = charge['outcome']
			src = charge['source']
			tf = int(charge['total_fee'])/100
			tft = int(charge['total_fee_taxes'])/100
			ItemPago.objects.filter(CodigoPublico=CodigoPublico).update(
			CodigoReferencia=charge['reference_code'],
			NroTarjeta=src['card_number'],
			FechaPago=datetime.now() - timedelta(hours=5),
			Estado= True,
			EstadoPago=True,
			CulqiMessage=oc['type'],
			CulqiRefCode=charge['reference_code'],
			CulqiStatus=oc['code'],
			CulqiAuthCode=charge['authorization_code'],
			CulqiFee =tf,
			CulqiFeeTaxes =tft
			)
			itemdata = get_object_or_404(ItemPago, CodigoPublico=CodigoPublico)
			html="vil/tpl/pagourl.html"
			mensaje = "<p style='color: #706a6a;'> {} </p><p>{}</p><p> <strong>Orden de Compra: </strong><span>{}</span> </p><p> <strong>C&oacute;digo de Referencia: </strong><span>{}</span> </p><p> <strong>Tarjeta de pago: </strong><span>{}</span> </p><p> <strong>Monto Pagado: </strong><span>S/{}</span> </p>".format(itemdata.FechaPago,itemdata.NombrePago,str(itemdata.id).zfill(5),itemdata.CodigoReferencia,itemdata.NroTarjeta,itemdata.Monto)
			noms = "{}".format(itemdata.Cliente)
			SentMail("PAGOURL - VILSOFT", mail, mensaje, noms, html)
		return JsonResponse(charge, safe=False)
	return JsonResponse("only POST method", safe=False)


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


def CotizacionPDF(request, id):
	from django.http import HttpResponse
	from django.template.loader import render_to_string
	from django.utils.text import slugify
	from django.contrib.auth.decorators import login_required
	from weasyprint import HTML
	from weasyprint.fonts import FontConfiguration
	from weasyprint import CSS
	bou = get_object_or_404(CotizacionCabecera, id=id)
	cuerpo = CuerpoCotizacion.objects.filter(cabecera=bou)
	print(bou.id)
	sum = 0
	for a in cuerpo:
		total=a.precio*a.cantidad
		sum = sum + total

	#response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
	response = HttpResponse(content_type="application/pdf")
	# response['Content-Disposition'] = "attachment;
	response['Content-Disposition'] = "attachment; filename=VLF.{}.{}.{}.pdf".format(bou.FechaCreacion.year,str(bou.ContSerializeQtn).zfill(4),str(bou.SerializeQtn).zfill(2))
	font_config = FontConfiguration()
	html = render_to_string("vil/tpl/cotizacion.html", {
		'bou': bou,
		'cuerpo': cuerpo,
		'request':request,
		"subtotal":sum
	})
	css = CSS(string='''
	@page {
		@bottom-center {
			content: string(title);
			font-size:12px;
			border-top:1px solid black;
			color:#186a43;
			width:100%;
			height:50px;
		}
		}
	header {
		width: 0;
		height: 0;
		visibility: hidden;
		string-set: title content();
	}
	@font-face {
		font-family: "calibrilight";
	}
	body{
		font-family: 'calibrilight';
		font-size: 12px;
	}''', font_config=font_config)
	HTML(string=html).write_pdf(response, stylesheets=[css], font_config=font_config)
	return response
