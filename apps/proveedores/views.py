from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render

from apps.proveedores.models import Proveedor
from apps.proveedores.forms import ProveedorForm

# Create your views here.
def DetalleProveedor(request):
	pro = Proveedor.objects.all()
	context = {"Proveedor":pro}
	return render(request, "proveedor/detalle.html", context)


def RegistrarProveedores(request):
	form = ProveedorForm(request.POST or None)
	if(request.method=='POST'):
		formResult=form.save()
		if(form.is_valid()):
			form.save()
			return redirect('proveedores:DetalleProveedor')
	context = {'form':form}
	return render(request, 'proveedor/registro.html', context)


def EditarProveedores(request, id):
	pro = get_object_or_404(Proveedor, id=id)
	form = ProveedorForm(request.POST or None,instance=pro)
	if request.method == "POST":
		if form.is_valid():
			form.save()
			return redirect("proveedores:DetalleProveedor")
	context = {"form":form,"id":id}
	return render(request, "proveedor/editar.html", context)

def DeleteProveedor(request, id):
	pro = get_object_or_404(Proveedor, id=id)
	aeliminar = ['Eliminar Proveedor','Realmente Desea eliminar el proveedor <strong>{}</strong>?<br><strong><small>Esta acción no se puede deshacer</small></strong>'.format(str(pro.RazonSocial))]
	if request.method=='POST':
		Proveedor.objects.filter(id=id).delete()
		messages.success(request, 'Se eliminó el Proveedor SATISFACTORIAMENTE.')
		return redirect('proveedores:DetalleProveedor')
	context = {"aeliminar":aeliminar, 'atras':request.META.get('HTTP_REFERER')}
	return render(request,'base/deleteform.html',context)
