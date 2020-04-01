from django import forms
from apps.cotizaciones.models import CotizacionCabecera
from apps.cotizaciones.models import CuerpoCotizacion
from apps.general.models import Moneda
# from apps.clientes.models import Clientes

class QtnEditForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(QtnEditForm, self).__init__(*args, **kwargs)
		self.fields['Moneda']=forms.ModelChoiceField(queryset=Moneda.objects.filter(),initial=0)
		self.fields['Moneda'].widget.attrs.update({'class': 'custom-select'})
		self.fields['TiempoEntrega'].widget.attrs.update({'class': 'form-control'})
		self.fields['Asunto'].widget.attrs.update({'class': 'form-control'})
		self.fields['Descripcion'].widget.attrs.update({'class': 'form-control',"rows":10})

	class Meta:
		model = CotizacionCabecera
		fields = [
		'Moneda',
		'TiempoEntrega',
		'Asunto',
		'Descripcion',
		]

class QtnForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(QtnForm, self).__init__(*args, **kwargs)
		self.fields['ContSerializeQtn'].widget.attrs.update({'class': 'form-control '})
		self.fields['SerializeQtn'].widget.attrs.update({'class': 'form-control'})
		# self.fields['Cliente']=forms.ModelChoiceField(queryset=Clientes.objects.filter(),initial=0)
		# self.fields['Cliente'].widget.attrs.update({'class': 'custom-select'})
		self.fields['Moneda']=forms.ModelChoiceField(queryset=Moneda.objects.filter(),initial=0)
		self.fields['Moneda'].widget.attrs.update({'class': 'custom-select'})
		self.fields['TiempoEntrega'].widget.attrs.update({'class': 'form-control'})
		# self.fields['Estado'].widget.attrs.update({'class': 'form-control'})
		self.fields['Asunto'].widget.attrs.update({'class': 'form-control'})
		self.fields['Descripcion'].widget.attrs.update({'class': 'form-control',"rows":4})
		# self.fields['Estudio'].widget.attrs.update({'class': 'form-control'})

	#Asunto = forms.ModelMultipleChoiceField(queryset=AsuntoCotizacion.objects.all(), widget=forms.CheckboxSelectMultiple())
	class Meta:
		model = CotizacionCabecera
		fields = [
		'ContSerializeQtn',
		'SerializeQtn',
		# 'Cliente',
		'Moneda',
		'TiempoEntrega',
		'Asunto',
		'Descripcion',
		]
		# labels  = {
		# 'Cliente'="",
		# 'Moneda',
		# 'TiempoEntrega',
		# 'ValidezOferta',
		# 'Asunto'
		# }


class DescuentoForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(DescuentoForm, self).__init__(*args, **kwargs)
		self.fields['Descuento'].widget.attrs.update({'class': 'form-control'})

	class Meta:
		model = CotizacionCabecera
		fields = [
		'Descuento',
		]
		labels = {
			'Descuento':"Descuento",
		}

class CuerpoCotizacionForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CuerpoCotizacionForm, self).__init__(*args, **kwargs)
		self.fields['cabecera'].widget.attrs.update({'class': 'form-control'})
		self.fields['item'].widget.attrs.update({'class': 'form-control'})
		self.fields['cantidad'].widget.attrs.update({'class': 'form-control'})
		self.fields['precio'].widget.attrs.update({'class': 'form-control'})

	class Meta:
		model = CuerpoCotizacion
		fields = [
		'cabecera',
		'item',
		'cantidad',
		'precio',
		]
