from django import forms
from apps.items.models import Producto
from apps.proveedores.models import Proveedor


class ItemsForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ItemsForm, self).__init__(*args, **kwargs)
		self.fields['SerializeProducto'].widget.attrs.update({'class': 'form-control '})
		self.fields['Nombre'].widget.attrs.update({'class': 'form-control '})
		self.fields['Foto'].widget.attrs.update({'class': 'form-control'})
		self.fields['TipoProducto'].widget.attrs.update({'class': 'custom-select'})
		self.fields['Descripcion'].widget.attrs.update({'class': 'form-control'})
		self.fields['Precio'].widget.attrs.update({'class': 'form-control'})
		self.fields['PrecioCompra'].widget.attrs.update({'class': 'form-control'})
		# self.fields['ProveedorItem']=forms.ModelChoiceField(queryset=Proveedor.objects.filter(),initial=0)
		# self.fields['ProveedorItem'].widget.attrs.update({'class': 'custom-select'})

	class Meta:
		model = Producto
		fields = [
		'SerializeProducto',
		'Nombre',
		'Foto',
		'TipoProducto',
		'Descripcion',
		'Precio',
		'PrecioCompra',
		# 'ProveedorItem',
		]
		# labels  = {
		# 'Cliente'="",
		# 'Moneda',
		# 'TiempoEntrega',
		# 'ValidezOferta',
		# 'Asunto'
		# }

class ItemsEditForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ItemsEditForm, self).__init__(*args, **kwargs)
		self.fields['SerializeProducto'].widget.attrs.update({'class': 'form-control '})
		self.fields['Nombre'].widget.attrs.update({'class': 'form-control '})
		self.fields['Foto'].widget.attrs.update({'class': 'form-control'})
		self.fields['TipoProducto'].widget.attrs.update({'class': 'custom-select'})
		self.fields['Descripcion'].widget.attrs.update({'class': 'form-control'})
		self.fields['Precio'].widget.attrs.update({'class': 'form-control'})
		self.fields['PrecioCompra'].widget.attrs.update({'class': 'form-control'})
		self.fields['ProveedorItem']=forms.ModelChoiceField(queryset=Proveedor.objects.filter(),initial=0)
		self.fields['ProveedorItem'].widget.attrs.update({'class': 'custom-select'})

	class Meta:
		model = Producto
		fields = [
		'SerializeProducto',
		'Nombre',
		'Foto',
		'TipoProducto',
		'Descripcion',
		'Precio',
		'PrecioCompra',
		'ProveedorItem',
		]
