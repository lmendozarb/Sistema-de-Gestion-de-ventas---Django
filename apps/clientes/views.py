from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render


from apps.clientes.models import Clientes
from apps.clientes.models import Contacto

from apps.clientes.forms import ClientesForm
from apps.clientes.forms import ContactoForm

# Create your views here.
def detallecliente(request):
	cli = Clientes.objects.all()
	context = {"Clientes":cli}
	return render(request, "cliente/detalle.html", context)


def registrarclientes(request):
	form = ClientesForm(request.POST or None)
	if(request.method=='POST'):
		formResult=form.save()
		if(form.is_valid()):
			form.save()
			return redirect('clientes:detallecliente')
	context = {'form':form}
	return render(request, 'cliente/registro.html', context)


def editarclientes(request, id):
	cli = get_object_or_404(Clientes, id = id)
	form = ClientesForm(request.POST or None,request.FILES or None,instance=cli)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('clientes:detallecliente')
		else:
			return redirect('clientes:registrarclientes', id=id)
	Contactos = Contacto.objects.all()
	context = {'form':form,"Contactos":Contactos,"cli":cli}
	return render(request, 'cliente/registro.html', context)


def registrarcontactos(request, id):
	form = ContactoForm(request.POST or None)
	if(request.method=='POST'):
		formResult=form.save()
		if form.is_valid():
			con = Contacto(formResult)
			cli = get_object_or_404(Clientes, id = id)
			cli.ContactoClientes.add(con.id)
			return redirect('clientes:editarclientes',id=id)
	Contactos = Contacto.objects.all()
	context = {'form':form, 'id':id,"Contactos":Contactos}
	return render(request, 'cliente/registrarcontacto.html', context)


def editarcontactos(request, id,idcont):
	con = get_object_or_404(Contacto, id=idcont)
	form = ContactoForm(request.POST or None,instance=con)
	if request.method == "POST":
		if form.is_valid():
			form.save()
			return redirect("clientes:editarclientes", id)
	context = {"form":form,"id":id}
	return render(request, "cliente/registrarcontacto.html", context)


def deletecontactos(request, id, idcont):
	con = get_object_or_404(Contacto, id=idcont)
	aeliminar = ['Eliminar contacto','Realmente Desea eliminar el contacto <strong>{}</strong>?<br><strong><small>Esta acción no se puede deshacer</small></strong>'.format(str(con.NombreContacto))]
	if request.method=='POST':
		Contacto.objects.filter(id=idcont).delete()
		messages.success(request, 'Se eliminó el contacto del cliente SATISFACTORIAMENTE.')
		return redirect('clientes:editarclientes',id=id)
	context = {"aeliminar":aeliminar, 'atras':request.META.get('HTTP_REFERER')}
	return render(request,'base/deleteform.html',context)


def Deleteclientes(request, id):
	con = get_object_or_404(Clientes, id=id)
	aeliminar = ['Eliminar Cliente','Realmente Desea eliminar el cliente <strong>{}</strong>?<br><strong><small>Esta acción no se puede deshacer</small></strong>'.format(str(con.RazonSocial))]
	if request.method=='POST':
		Clientes.objects.filter(id=id).delete()
		messages.success(request, 'Se eliminó el contacto del cliente SATISFACTORIAMENTE.')
		return redirect('clientes:detallecliente')
	context = {"aeliminar":aeliminar, 'atras':request.META.get('HTTP_REFERER')}
	return render(request,'base/deleteform.html',context)
