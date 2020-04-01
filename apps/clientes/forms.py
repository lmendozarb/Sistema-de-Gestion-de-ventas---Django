from django import forms
from apps.clientes.models import Clientes
from apps.clientes.models import Contacto
from apps.general.models import TipoDocumento

class ClientesForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ClientesForm, self).__init__(*args, **kwargs)
		self.fields['RazonSocial'].widget.attrs.update({'class': 'form-control'})
		self.fields['Website'].widget.attrs.update({'class': 'form-control'})
		self.fields['CorreoElectronico'].widget.attrs.update({'class': 'form-control'})
		self.fields['TipoPersona']=forms.ChoiceField(choices=Clientes.STATUS_CHOICES)
		self.fields['TipoPersona'].widget.attrs.update({'class': 'custom-select'})
		self.fields['RUC'].widget.attrs.update({'class': 'form-control'})
		self.fields['DireccionLegal'].widget.attrs.update({'class': 'form-control'})
		self.fields['LegalName'].widget.attrs.update({'class': 'form-control'})
		self.fields['LegalLastName'].widget.attrs.update({'class': 'form-control'})
		self.fields['TipoDocumentoLegal']=forms.ModelChoiceField(queryset=TipoDocumento.objects.filter(),initial=0)
		self.fields['TipoDocumentoLegal'].widget.attrs.update({'class': 'custom-select'})
		self.fields['NroDocumentoLegal'].widget.attrs.update({'class': 'form-control'})

	class Meta:
		model = Clientes
		fields = [
		'RazonSocial',
		'Website',
		'CorreoElectronico',
		'TipoPersona',
		'RUC',
		'DireccionLegal',
		'LegalName',
		'LegalLastName',
		'TipoDocumentoLegal',
		'NroDocumentoLegal',
		]
		labels={
		'RazonSocial':"Razón Social / Nombre del Cliente",
		'Website':"Sitio WEB",
		'CorreoElectronico':"Correo Electrónico",
		'TipoPersona':"Tipo de Empresa",
		'RUC':"RUC",
		'DireccionLegal':"Dirección Fiscal",
		'LegalName':"Nombres Representante Legal",
		'LegalLastName':"Apellidos Representante Legal",
		'TipoDocumentoLegal':"Tipo Documento",
		'NroDocumentoLegal':"Nro. Documento",
		}

class ContactoForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ContactoForm, self).__init__(*args, **kwargs)
		self.fields['NombreContacto'].widget.attrs.update({'class': 'form-control'})
		self.fields['TipoDocumentoContacto']=forms.ModelChoiceField(queryset=TipoDocumento.objects.filter(),initial=0)
		self.fields['ApellidoContacto'].widget.attrs.update({'class': 'form-control'})
		self.fields['TipoDocumentoContacto'].widget.attrs.update({'class': 'custom-select'})
		self.fields['NroDocumentoContacto'].widget.attrs.update({'class': 'form-control'})
		self.fields['CorreoElectronicoContacto'].widget.attrs.update({'class': 'form-control'})
		self.fields['MovilContacto'].widget.attrs.update({'class': 'form-control'})
		self.fields['LugarTrabajo'].widget.attrs.update({'class': 'form-control'})
		self.fields['Cargo'].widget.attrs.update({'class': 'form-control'})
		self.fields['Principal'].widget.attrs.update({'class': 'form-check-inline'})

	class Meta:
		model = Contacto
		fields = [
		'NombreContacto',
		'ApellidoContacto',
		'TipoDocumentoContacto',
		'NroDocumentoContacto',
		'CorreoElectronicoContacto',
		'MovilContacto',
		'LugarTrabajo',
		'Cargo',
		'Principal',
		]
		labels={
		'NombreContacto':"Nombre de Contacto",
		'ApellidoContacto':"Apellidos de Contacto",
		'TipoDocumentoContacto':"Tipo Documento",
		'NroDocumentoContacto':"Nro. Documento",
		'CorreoElectronicoContacto':"Correo Electrónico de Contacto",
		'MovilContacto':"Nro. Teléfono Móvil",
		'LugarTrabajo':"Lugar de Trabajo",
		'Cargo':"Cargo",
		'Principal':"¿Es Contacto Principal?",
		}

class ContactoPrincipalForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ContactoPrincipalForm, self).__init__(*args, **kwargs)

		self.fields['Principal'].widget.attrs.update({'class': 'form-check-inline'})

	class Meta:
		model = Contacto
		fields = [
		'Principal',
		]
		labels={
		'Principal':"¿Es Contacto Principal?",
		}
