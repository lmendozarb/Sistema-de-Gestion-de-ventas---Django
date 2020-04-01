from django import forms
from apps.ordencompra.models import OrdenCabecera
from apps.ordencompra.models import OrdenCompraBody
from apps.ordencompra.models import OrdenCompraCierre
from apps.proveedores.models import Proveedor
from apps.items.models import Producto


class CompraForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CompraForm, self).__init__(*args, **kwargs)
		self.fields['ContSerializeQtn'].widget.attrs.update({'class': 'form-control'})
		self.fields['SerializeQtn'].widget.attrs.update({'class': 'form-control'})
		self.fields['CondicionVenta'].widget.attrs.update({'class': 'form-control'})
		self.fields['Proveedor']=forms.ModelChoiceField(queryset=Proveedor.objects.filter())
		self.fields['Proveedor'].widget.attrs.update({'class': 'form-control'})
	class Meta:
		model = OrdenCabecera
		fields = [
		'ContSerializeQtn',
		'SerializeQtn',
		"CondicionVenta",
		"Proveedor",
		]


class CompraBodyForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CompraBodyForm, self).__init__(*args, **kwargs)
		self.fields['CompraHead'].widget.attrs.update({'class': 'form-control'})
		self.fields['Item'].widget.attrs.update({'class': 'form-control'})
		self.fields['Cantidad'].widget.attrs.update({'class': 'form-control'})
	class Meta:
		model = OrdenCompraBody
		fields = [
		"CompraHead",
		"Item",
		"Cantidad",
		]
		labels={
			"Cantidad" :  "Cantidad",
		}

class CompraCierreForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CompraCierreForm, self).__init__(*args, **kwargs)
		self.fields['FacturaCompraFisico'].widget.attrs.update({'class': 'form-control'})
		self.fields['GuiadeRemisionFisico'].widget.attrs.update({'class': 'form-control'})
		self.fields['CompraHead'].widget.attrs.update({'class': 'form-control'})
	class Meta:
		model = OrdenCompraCierre
		fields = [
		"FacturaCompraFisico",
		"GuiadeRemisionFisico",
		"CompraHead"
		]
		labels={
			"FacturaCompraFisico" : "Factura de compra",
			"GuiadeRemisionFisico" : "Guia de Remision Fisica",
		}
