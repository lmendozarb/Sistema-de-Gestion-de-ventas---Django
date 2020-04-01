from django import forms

from apps.general.models import Moneda
from apps.general.models import TipoDocumento


class MonedaForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(MonedaForm, self).__init__(*args, **kwargs)
		self.fields['Moneda'].widget.attrs.update({'class': 'form-control'})
		self.fields['Plural'].widget.attrs.update({'class': 'form-control'})
		self.fields['Signo'].widget.attrs.update({'class': 'form-control'})
		self.fields['Denominacion'].widget.attrs.update({'class': 'form-control'})

	class Meta:
		model = Moneda
		fields = [
		'Moneda',
		'Plural',
		'Signo',
		'Denominacion',
		]


class DocumentoForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(DocumentoForm, self).__init__(*args, **kwargs)
		self.fields['Name'].widget.attrs.update({'class': 'form-control'})
		self.fields['Abreviatura'].widget.attrs.update({'class': 'form-control'})

	class Meta:
		model = TipoDocumento
		fields = [
		'Name',
		'Abreviatura',
		]
