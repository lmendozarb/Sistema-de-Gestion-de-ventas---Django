from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages

from apps.items.models import Producto
from apps.items.forms import ItemsForm
from apps.items.forms import ItemsEditForm
from apps.proveedores.forms import Proveedor

# Create your views here.
def DetalleProducto(request):
	pro = Producto.objects.all()
	context = {"Producto":pro}
	return render(request, "items/detalle.html", context)

def RegistroProducto(request):
	prove=Proveedor.objects.all()
	form = ItemsForm(request.POST,request.FILES or None)
	if request.method=='POST':
		formResult=form.save()
		if form.is_valid() :
			formResult = form.save(commit=False)
			proveedor = request.POST.get('Proveedor', None)
			pro = proveedor.split("-")
			prov = Proveedor.objects.get(id=pro[0])
			formResult.ProveedorItem = prov
			pr = Producto.objects.all().order_by("-SerializeProducto")[0]
			corr = pr.SerializeProducto + 1
			formResult.SerializeProducto = corr
			formResult.save()
			messages.success(request, 'Se registró el item SATISFACTORIAMENTE.')
			return redirect('items:DetalleProducto')
		else:
			print(form)
	context = {'form':form,'proveedor':prove}
	return render(request, 'items/registraritems.html', context)

def EditarProducto(request, id):
	pro = get_object_or_404(Producto, id=id)
	form = ItemsEditForm(request.POST or None,request.FILES or None,instance=pro)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			messages.success(request, 'Se registró el item SATISFACTORIAMENTE.')
			return redirect('items:DetalleProducto')
	context = {'form':form,"pro":pro}
	return render(request, "items/editaritems.html", context)

def ElminarProducto(request, id):
	pro = get_object_or_404(Producto, id=id)
	aeliminar = ['Eliminar Item','Realmente Desea eliminar el item <strong>{}</strong>?<br><strong><small>Esta acción no se puede deshacer</small></strong>'.format(str(pro.Nombre))]
	if request.method=='POST':
		Producto.objects.filter(id=id).delete()
		messages.success(request, 'Se eliminó el Item SATISFACTORIAMENTE.')
		return redirect('items:DetalleProducto')
	context = {"aeliminar":aeliminar, 'atras':request.META.get('HTTP_REFERER')}
	return render(request,'base/deleteform.html',context)
