from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.utils.html import strip_tags
from django.template.loader import render_to_string

from apps.ordencompra.models import OrdenCabecera
from apps.ordencompra.models import OrdenCompraBody
from apps.ordencompra.models import OrdenCompraCierre
from apps.ordencompra.forms import CompraForm
from apps.ordencompra.forms import CompraBodyForm
from apps.ordencompra.forms import CompraCierreForm
from apps.items.models import Producto
from apps.proveedores.models import Proveedor
# Create your views here.

def DetalleCompra(request):
	com = OrdenCabecera.objects.all().order_by('-id')
	context = {"Compra":com}
	return render(request, "ordencompra/detalle.html",context)


def OrdenCompra(request,id):
	compra= OrdenCabecera.objects.get(id=id)
	item = OrdenCompraBody.objects.filter(CompraHead=compra.id)
	prove=get_object_or_404(Proveedor, id=compra.Proveedor.id)
	produc=Producto.objects.filter(ProveedorItem=prove.id)
	sum = 0
	for a in item:
		total=a.Item.PrecioCompra*a.Cantidad
		sum = sum + total
	context = {"Item":item, "Compra" : compra,'id':id,'producto':produc,'subtotal':sum}
	return render(request, "ordencompra/ordenbody.html",context)


def CreateCompra(request):
	form = CompraForm(request.POST, request.FILES or None)
	if request.method=='POST':
		formResult=form.save()
		if form.is_valid():
			formResult = form.save(commit=False)
			bf = OrdenCabecera.objects.all().order_by("-ContSerializeQtn")[0]
			corr = bf.ContSerializeQtn + 1
			formResult.ContSerializeQtn = corr
			formResult.Estado="CONFIRMAR"
			formResult.save()
			messages.success(request, 'Se creó una nueva Compra SATISFACTORIAMENTE.')
			return redirect('ordencompra:OrdenCompra', id=formResult.id)
	context = {'form':form}
	return render(request, 'ordencompra/registrarcompra.html', context)


def AnulateOrden(request, id):
	if request.user.is_superuser or request.user.groups.filter(name="Administrador").exists():
		cabe = OrdenCabecera.objects.filter(id=id).update(Estado="ANULAR")
		messages.success(request, 'Se Anuló la Orden de compra SATISFACTORIAMENTE.')
		return redirect('ordencompra:OrdenCompra', id)


def RegistrarItem(request, id, iditem):
	form = CompraBodyForm(request.POST or None)
	if(request.method=='POST'):
		formResult=form.save()
		if(form.is_valid()):
			frore = form.save(commit=False)
			cabe = get_object_or_404(OrdenCabecera,id=id)
			frore.CompraHead = cabe
			produc = get_object_or_404(Producto,id=iditem)
			frore.Item = produc
			frore.save()
			return redirect('ordencompra:OrdenCompra',id=id)
	context = {'form':form,"id":id,"iditem":iditem}
	return render(request, 'ordencompra/registraritem.html', context)


def CierreOrden(request,id):
	form = CompraCierreForm(request.POST or None)
	if request.method=='POST':
		if form.is_valid():
			formResult=form.save(commit=False)
			orden=get_object_or_404(OrdenCabecera,id=id)
			formResult.CompraHead = orden
			OrdenCabecera.objects.filter(id=id).update(Estado="FACTURADO")
			compra= OrdenCabecera.objects.get(id=id)
			item = OrdenCompraBody.objects.filter(CompraHead=compra.id)
			prove=get_object_or_404(Proveedor, id=compra.Proveedor.id)
			produc=Producto.objects.filter(ProveedorItem=prove.id)
			sum = 0
			for com in item:
				for producto2 in produc:
					if com.Item.id == producto2.id:
						sum = com.Cantidad + producto2.Cantidad
						Producto.objects.filter(id=producto2.id).update(Cantidad=sum)
			formResult.save()
			messages.success(request, 'Se Genero la Orden de compra SATISFACTORIAMENTE.')
			return redirect('ordencompra:OrdenCompra',id)
	context = {'form':form,'id':id}
	return render(request, 'ordencompra/ordencierre.html', context)

def OdenPDF(request, id):
	from django.http import HttpResponse
	from django.template.loader import render_to_string
	from django.utils.text import slugify
	from django.contrib.auth.decorators import login_required
	from weasyprint import HTML
	from weasyprint.fonts import FontConfiguration
	from weasyprint import CSS
	compra= OrdenCabecera.objects.get(id=id)
	item = OrdenCompraBody.objects.filter(CompraHead=compra.id)
	prove=get_object_or_404(Proveedor, id=compra.Proveedor.id)
	produc=Producto.objects.filter(ProveedorItem=prove.id)
	sum = 0
	for a in item:
		total=a.Item.PrecioCompra*a.Cantidad
		sum = sum + total

	#response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
	response = HttpResponse(content_type="application/pdf")
	# response['Content-Disposition'] = "attachment;
	response['Content-Disposition'] = "attachment; filename=ODE.{}.{}.{}.pdf".format(compra.FechaCreacion.year,str(compra.ContSerializeQtn).zfill(4),str(compra.SerializeQtn).zfill(2))
	font_config = FontConfiguration()
	html = render_to_string("vil/tpl/ordendecompra.html", {
		'compra': compra,
		'Item': item,
		'request':request,
		'prove':prove,
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
